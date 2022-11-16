from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import (
    CallbackContext, ConversationHandler, Updater,
    MessageHandler, CallbackQueryHandler, Filters,
    CommandHandler)

from accounts.models import User
from classrooms.models import Schedule
from courses.models import Course
from telegrambot.models import BotAnswer

from classrooms.services import StudentService, ClassroomService

from telegrambot.handlers.login_handler import LoginHandler

from telegram import Update
from telegram import ParseMode

from django.utils import dateformat

import telegram


class StudentHandler:
    """
    Класс с функциями для действий студента
    """

    HOMEWORK_URL = range(1)

    @staticmethod
    def _send_courses_list(update: Update.callback_query):
        """
        Отправляет студенту курсы на которых он учится
        """

        user = User.objects.get(telegram_id=update.message.chat_id)
        user_courses = StudentService.get_student_courses(user)

        if not user_courses:
            update.message.reply_text('Ты еще на записан на курсы 😢')
            return

        reply_markup = InlineKeyboardMarkup.from_column(
            [InlineKeyboardButton(
                i.get('course__title'), callback_data=f"ModulesList {i.get('course_id')}"
            ) for i in user_courses]
        )

        update.message.reply_text('Список твоих курсов 📝', reply_markup=reply_markup)

    @staticmethod
    def _send_modules_list(update: Update.callback_query, course_id):
        """
        Отправляет студенту модули выбранного курса
        """

        course = Course.objects.get(id=course_id)

        reply_markup = InlineKeyboardMarkup.from_column(
            [InlineKeyboardButton(
                module.title, callback_data=f'LessonsList {module.id} {course_id}'
            ) for module in course.modules.all()] + [InlineKeyboardButton('Назад ⏪', callback_data='CoursesList')]
        )

        update.message.reply_text('Модули в этом курсе 📝', reply_markup=reply_markup)

    @staticmethod
    def _send_lessons_list(update: Update.callback_query, module_id, course_id):
        """
        Отправляет студенту уроки из его расписания
        """

        user = User.objects.get(telegram_id=update.message.chat_id)
        user_lessons = StudentService.get_student_lessons(user, module_id, course_id)

        back_button = [InlineKeyboardButton('Назад ⏪', callback_data=f'ModulesList {course_id}')]

        if not user_lessons:
            reply_markup = InlineKeyboardMarkup.from_column(back_button)
            update.message.reply_text('У тебя еще не было уроков по этому модулю 😢', reply_markup=reply_markup)
            return

        reply_markup = InlineKeyboardMarkup.from_column(
            [InlineKeyboardButton(
                i.get('lesson__title'), callback_data=f"LessonsView {i.get('id')} lessons_list"
            ) for i in user_lessons] + back_button
        )

        update.message.reply_text('Прошедшие уроки 📚', reply_markup=reply_markup)

    @staticmethod
    def _send_lessons_info(update: Update.callback_query, schedule_id, back_location):
        """
        Отправляет студенту выбранный урок (материалы, статус задания)
        """

        user = User.objects.get(telegram_id=update.message.chat_id)
        schedule = Schedule.objects.get(id=schedule_id)

        schedule_title = schedule.lesson.title.replace('.', '\.').replace('-', '\-')
        hw_status = 'Не сдано'

        message = f"*Урок:* _{schedule_title}_\n"

        keyboard = [InlineKeyboardButton('Материалы урока 📒', url=schedule.lesson.document_url)]

        if schedule.homeworks.filter(student=user).exists():
            homework = schedule.homeworks.get(student=user)

            if homework.is_accepted:
                hw_status = 'Зачтено'
            elif homework.need_to_fix:
                hw_status = 'Доработать'
                keyboard.append(InlineKeyboardButton('Исправить задание 📄', callback_data=f'HomeworksSend {schedule.id}'))
            else:
                hw_status = 'На проверке'
                keyboard.append(InlineKeyboardButton('Изменить ссылку 🔗', callback_data=f'HomeworksSend {schedule.id}'))
        else:
            keyboard.append(InlineKeyboardButton('Сдать задание 📄', callback_data=f'HomeworksSend {schedule.id}'))

        message += f'*Домашнее задание:* _{hw_status}_'

        callback_data = 'HomeworksList'

        if back_location == 'lessons_list':
            callback_data = f'LessonsList {schedule.lesson.module_id} {schedule.classroom.course_id}'

        keyboard.append(InlineKeyboardButton(text='Назад ⏪', callback_data=callback_data))

        reply_markup = InlineKeyboardMarkup.from_column(keyboard)
        update.message.reply_markdown_v2(message, reply_markup=reply_markup)

    @staticmethod
    def _send_homeworks_list(update: Update.callback_query):
        """
        Отправляет студенту уроки, требующие сдать задание из его расписания
        """

        user = User.objects.get(telegram_id=update.message.chat_id)
        user_lessons = StudentService.get_student_lessons(user, wait_homework=True)

        if not user_lessons:
            update.message.reply_text('Нет заданий требующих сдачи 🥰')
            return

        reply_markup = InlineKeyboardMarkup.from_column(
            [InlineKeyboardButton(
                i.get('lesson__title'), callback_data=f"LessonsView {i.get('id')} homeworks_list"
            ) for i in user_lessons]
        )

        update.message.reply_text('Домашнее задание к этим урокам можно сдать 📚', reply_markup=reply_markup)

    @staticmethod
    def _send_student_schedule(update: Update):
        """
        Отправляет студенту его расписание
        """

        user = User.objects.get(telegram_id=update.message.chat_id)
        schedule = ClassroomService.get_user_schedule(user, 7)

        if not schedule:
            update.message.reply_text('Ближайших занятий нет 🥰')
            return

        message = 'Твои ближайшие занятия 📔\n'

        for lesson in schedule:
            title = lesson.get('lesson__title').replace('.', '\.').replace('-', '\-')

            date_of_lesson = lesson.get('date_of_lesson')

            date = dateformat.format(date_of_lesson, 'd E')
            time = dateformat.time_format(date_of_lesson, 'H:i')

            message += f'\n*{title}*: _{date} {time} МСК_'

        update.message.reply_markdown_v2(message)

    @staticmethod
    def _homeworks_send(update: Update, context: CallbackContext):
        """
        Отправка домашнего задания
        """

        schedule_id = context.user_data.get('schedule_id')
        task_url = update.message.text

        if not schedule_id:
            update.message.reply_text('Как такое случилось? Ошибка 😢')
            return ConversationHandler.END

        user = User.objects.get(telegram_id=update.message.chat_id)
        result = StudentService.send_student_homework(user, schedule_id, task_url)

        if result:
            update.message.reply_text(BotAnswer.objects.get(query='Работа отправлена').text)

            schedule = Schedule.objects.get(id=schedule_id)

            if schedule.teacher.telegram_id:
                full_name = f'{user.first_name} {user.last_name}'
                classroom = schedule.classroom.title.replace('.', '\.').replace('-', '\-')
                lesson = schedule.lesson.title.replace('.', '\.').replace('-', '\-')

                message = f'Студент *{full_name}* из группы *{classroom}* ' \
                          f'отправил домашнее задание по уроку *{lesson}* 🥰'

                context.bot.send_message(
                    chat_id=schedule.teacher.telegram_id,
                    text=message,
                    parse_mode=ParseMode.MARKDOWN_V2)

            return ConversationHandler.END

        update.message.reply_text(BotAnswer.objects.get(query='Неверная ссылка').text)
        return StudentHandler.HOMEWORK_URL

    @classmethod
    def messages(cls, update: Update, context: CallbackContext):
        """
        Обработчик текстовых сообщений от нижнего меню
        """

        if not User.objects.filter(telegram_id=update.message.chat_id).exists():
            update.message.reply_text(BotAnswer.objects.get(query='Не понимаю').text)
            return

        user = User.objects.get(telegram_id=update.message.chat_id)

        message = update.message.text

        if user.type.id_name == 'student':
            if message == 'Мои курсы 💼':
                cls._send_courses_list(update)
            elif message == 'Сдать работу 🎒':
                cls._send_homeworks_list(update)
            elif message == 'Ближайшие занятия 📔':
                cls._send_student_schedule(update)
            else:
                update.message.reply_text(BotAnswer.objects.get(query='Не понимаю').text)

    @classmethod
    def callbacks(cls, update: Update, context: CallbackContext):
        """
        Обработчик inline клавиатуры под сообщениями
        """

        button_press = update.callback_query

        if 'CoursesList' in button_press.data:
            try:
                button_press.message.delete()
            except telegram.TelegramError:
                pass
            finally:
                cls._send_courses_list(button_press)
        elif 'ModulesList' in button_press.data:
            try:
                button_press.message.delete()
            except telegram.TelegramError:
                pass
            finally:
                course_id = button_press.data.split(' ')[1]
                cls._send_modules_list(button_press, course_id)
        elif 'LessonsList' in button_press.data:
            try:
                button_press.message.delete()
            except telegram.TelegramError:
                pass
            finally:
                module_id = button_press.data.split(' ')[1]
                course_id = button_press.data.split(' ')[2]
                cls._send_lessons_list(button_press, module_id, course_id)
        elif 'LessonsView' in button_press.data:
            try:
                button_press.message.delete()
            except telegram.TelegramError:
                pass
            finally:
                schedule_id = button_press.data.split(' ')[1]
                back_location = button_press.data.split(' ')[2]
                cls._send_lessons_info(button_press, schedule_id, back_location)
        elif 'HomeworksList' in button_press.data:
            try:
                button_press.message.delete()
            except telegram.TelegramError:
                pass
            finally:
                cls._send_homeworks_list(button_press)
        elif 'HomeworksSend' in button_press.data:
            try:
                button_press.message.delete()
            except telegram.TelegramError:
                pass
            finally:
                schedule_id = button_press.data.split(' ')[1]
                context.user_data['schedule_id'] = schedule_id
                button_press.message.reply_text('Отправь ссылку 📚')
                return StudentHandler.HOMEWORK_URL

    @classmethod
    def get_homework_handler(cls):
        """
        Возвращает homework_handler
        """

        homework_handler = ConversationHandler(
            entry_points=[CallbackQueryHandler(cls.callbacks, pattern='HomeworksSend')],
            states={
                StudentHandler.HOMEWORK_URL: [MessageHandler(Filters.text & ~Filters.command, cls._homeworks_send)],
            },
            fallbacks=[CommandHandler('cancel', LoginHandler.start)],
        )
        return homework_handler
