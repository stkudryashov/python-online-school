from django.core.management.base import BaseCommand

from telegram.ext import Updater, Defaults

from telegrambot.handlers.login_handler import *

import pytz


class Command(BaseCommand):
    def handle(self, *args, **options):
        defaults = Defaults(tzinfo=pytz.timezone('Europe/Moscow'))
        updater = Updater('token', defaults=defaults)

        dispatcher = updater.dispatcher
        dispatcher.add_handler(LoginHandler.get_login_handler())

        updater.start_polling()
        updater.idle()