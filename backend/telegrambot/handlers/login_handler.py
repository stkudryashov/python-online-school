from accounts.models import User
from telegrambot.models import BotAnswer

from telegram import Update

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from telegrambot.keyboards import LOGIN_BUTTON
from telegrambot.services import get_user_keyboard

from telegram.ext import CallbackContext, ConversationHandler, CommandHandler, MessageHandler, Filters


class LoginHandler:
    """
    Класс с функциями для входа в аккаунт пользователя
    """

    START_LOGIN, USER_EMAIL = range(2)

    @staticmethod
    def start(update: Update, context: CallbackContext):
        """
        Запускает сценарий входа в аккаунт или отправляет главное меню
        """

        if User.objects.filter(telegram_id=update.message.chat_id).exists():
            user = User.objects.get(telegram_id=update.message.chat_id)

            update.message.reply_text(
                'Личный кабинет 🖥',
                reply_markup=get_user_keyboard(user)
            )

            return ConversationHandler.END

        update.message.reply_text(
            text=BotAnswer.objects.get(query='Приветствие').text,
            reply_markup=LOGIN_BUTTON
        )

        return LoginStates.START_LOGIN

    @staticmethod
    def _login(update: Update, context: CallbackContext):
        """
        Запрашивает электронную почту
        """

        if update.message.text != 'Войти 🏫':
            update.message.reply_text(
                'Для входа в свой аккаунт нажми кнопку ниже ⬇️',
                reply_markup=LOGIN_BUTTON
            )

            return LoginHandler.START_LOGIN

        update.message.reply_text(BotAnswer.objects.get(query='Запрос почты').text)
        return LoginHandler.USER_EMAIL

    @staticmethod
    def _email(update: Update, context: CallbackContext):
        """
        Проверяет корректность почты, в случае успеха присваивает telegram_id
        """

        user_email = update.message.text

        try:
            validate_email(user_email)

            if not User.objects.filter(email=user_email, telegram_id__isnull=True).exists():
                update.message.reply_text(BotAnswer.objects.get(query='Почта не найдена').text)
                return LoginHandler.USER_EMAIL

            user = User.objects.get(email=user_email)

            user.telegram_id = update.message.chat_id
            user.save()

            update.message.reply_text(
                f'Добрый день, {user.first_name}!',
                reply_markup=get_user_keyboard(user)
            )

            return ConversationHandler.END
        except ValidationError:
            update.message.reply_text(BotAnswer.objects.get(query='Ошибка почты').text)
            return LoginHandler.USER_EMAIL

    @classmethod
    def get_login_handler(cls):
        """
        Возвращает login_handler
        """

        login_handler = ConversationHandler(
            entry_points=[CommandHandler('start', cls.start)],
            states={
                LoginHandler.START_LOGIN: [MessageHandler(Filters.text, cls._login)],
                LoginHandler.USER_EMAIL: [MessageHandler(Filters.text & ~Filters.command, cls._email)],
            },
            fallbacks=[CommandHandler('cancel', cls.start)],
        )
        return login_handler
