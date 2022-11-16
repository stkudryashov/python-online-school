from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import (
    CallbackContext, Updater,
    MessageHandler, CallbackQueryHandler,
    Filters)

from accounts.models import User
from classrooms.models import Schedule
from telegrambot.models import BotAnswer

from classrooms.services import TeacherService, ClassroomService

from telegram import Update

from django.utils import dateformat

import telegram


class TeacherHandler:
    """
    Класс с функциями для действий учителя
    """

    @staticmethod
    def _send_classrooms_list(update: Update.callback_query):
        """
        Отправляет преподавателю группы в которых у него есть занятия
        """

        user = User.objects.get(telegram_id=update.message.chat_id)
        user_classrooms = TeacherService.get_teacher_classrooms(user)

        if not user_classrooms:
            update.message.reply_text('Нет активных групп 😢')
            return

        reply_markup = InlineKeyboardMarkup.from_column(
            [InlineKeyboardButton(
                classroom.get('title'), callback_data=f"TeacherClassroom {classroom.get('id')}"
            ) for classroom in user_classrooms]
        )

        update.message.reply_text('Список твоих групп 👩‍🎨', reply_markup=reply_markup)

    @staticmethod
    def _send_teacher_lessons(update: Update.callback_query, classroom_id):
        """
        Отправляет преподавателю его занятия в выбранной группе
        """

        user = User.objects.get(telegram_id=update.message.chat_id)
        user_lessons = TeacherService.get_teacher_lessons(user, classroom_id)

        reply_markup = InlineKeyboardMarkup.from_column(
            [InlineKeyboardButton(
                lesson.get('lesson__title'), callback_data=f"TeacherLesson {classroom_id} {lesson.get('id')}"
            ) for lesson in user_lessons] + [InlineKeyboardButton('Назад ⏪', callback_data='ClassroomsList')]
        )

        update.message.reply_text('Активные занятия 💻', reply_markup=reply_markup)

    @staticmethod
    def _send_lesson_info(update: Update.callback_query, classroom_id, schedule_id):
        """
        Отправляет преподавателю информацию о выбранном занятии
        """

        schedule = Schedule.objects.get(id=schedule_id)

        title = schedule.lesson.title.replace('.', '\.').replace('-', '\-')
        date = dateformat.format(schedule.date_of_lesson, 'd E')
        time = dateformat.time_format(schedule.date_of_lesson, 'H:i')

        hw_all = schedule.classroom.studentclassroom_set.all().count()
        hw_waiting = schedule.homeworks.all().count()
        hw_accepted = schedule.homeworks.filter(is_accepted=True).count()

        message = f"*Урок:* _{title}_\n" \
                  f"*Дата урока:* _{date} {time} МСК_\n\n" \
                  f"*Отправили работы:* _{hw_waiting} / {hw_all}\n_" \
                  f"*Получили зачет:* _{hw_accepted}_"

        back_button = [InlineKeyboardButton('Назад ⏪', callback_data=f'TeacherClassroom {classroom_id}')]
        reply_markup = InlineKeyboardMarkup.from_column(back_button)

        update.message.reply_markdown_v2(message, reply_markup=reply_markup)

    @staticmethod
    def _send_teacher_schedule(update: Update):
        """
        Отправляет учителю его расписание
        """

        user = User.objects.get(telegram_id=update.message.chat_id)
        schedule = ClassroomService.get_user_schedule(user, 7)

        if not schedule:
            update.message.reply_text('Ближайших занятий нет 🥰')
            return

        message = 'Ближайшие занятия 📔\n'

        for lesson in schedule:
            title = lesson.get('lesson__title').replace('.', '\.').replace('-', '\-')

            date_of_lesson = lesson.get('date_of_lesson')

            date = dateformat.format(date_of_lesson, 'd E')
            time = dateformat.time_format(date_of_lesson, 'H:i')

            classroom = lesson.get('classroom__title').replace('.', '\.').replace('-', '\-')

            message += f'\n*{classroom}* \- *{title}*: _{date} {time} МСК_'

        update.message.reply_markdown_v2(message)

    @classmethod
    def messages(cls, update: Update, context: CallbackContext):
        """
        Обработчик текстовых сообщений от нижнего меню
        """

        user = User.objects.get(telegram_id=update.message.chat_id)
        message = update.message.text

        if user.type.id_name == 'teacher':
            if message == 'Мои студенты 🧑🏼‍🎓':
                cls._send_classrooms_list(update)
            elif message == 'Мои занятия 📆':
                cls._send_teacher_schedule(update)
            else:
                update.message.reply_text(BotAnswer.objects.get(query='Не понимаю').text)

    @classmethod
    def callbacks(cls, update: Update, context: CallbackContext):
        """
        Обработчик inline клавиатуры под сообщениями
        """

        button_press = update.callback_query

        if 'ClassroomsList' in button_press.data:
            try:
                button_press.message.delete()
            except telegram.TelegramError:
                pass
            finally:
                cls._send_classrooms_list(button_press)
        elif 'TeacherClassroom' in button_press.data:
            try:
                button_press.message.delete()
            except telegram.TelegramError:
                pass
            finally:
                classroom_id = button_press.data.split(' ')[1]
                cls._send_teacher_lessons(button_press, classroom_id)
        elif 'TeacherLesson' in button_press.data:
            try:
                button_press.message.delete()
            except telegram.TelegramError:
                pass
            finally:
                classroom_id = button_press.data.split(' ')[1]
                schedule_id = button_press.data.split(' ')[2]
                cls._send_lesson_info(button_press, classroom_id, schedule_id)
