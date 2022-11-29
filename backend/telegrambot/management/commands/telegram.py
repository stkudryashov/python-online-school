from django.core.management.base import BaseCommand

from telegram.ext import (
    Updater, Defaults, CommandHandler, MessageHandler,
    CallbackQueryHandler, Filters, CallbackContext)

from telegram import Update
from accounts.models import User

from telegrambot.handlers.login_handler import LoginHandler
from telegrambot.handlers.student_handler import StudentHandler
from telegrambot.handlers.teacher_handler import TeacherHandler

from telegrambot.models import BotAnswer

from telegrambot.services import change_user_type

import pytz


def messages(update: Update, context: CallbackContext):
    if not User.objects.filter(telegram_id=update.message.chat_id).exists():
        update.message.reply_text(BotAnswer.objects.get(query='Не понимаю').text)
        return

    StudentHandler.messages(update, context)
    TeacherHandler.messages(update, context)


def callbacks(update: Update, context: CallbackContext):
    StudentHandler.callbacks(update, context)
    TeacherHandler.callbacks(update, context)


class Command(BaseCommand):
    def handle(self, *args, **options):
        defaults = Defaults(tzinfo=pytz.timezone('Europe/Moscow'))
        updater = Updater('token', defaults=defaults)

        dispatcher = updater.dispatcher

        dispatcher.add_handler(LoginHandler.get_login_handler())
        dispatcher.add_handler(StudentHandler.get_homework_handler())

        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, messages))
        dispatcher.add_handler(CallbackQueryHandler(callbacks))

        # Смена типа своего аккаунта (только для superuser)
        dispatcher.add_handler(CommandHandler('type', change_user_type))

        updater.start_polling()
        updater.idle()
