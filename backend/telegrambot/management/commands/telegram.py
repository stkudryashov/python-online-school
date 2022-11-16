from django.core.management.base import BaseCommand

from telegram.ext import Updater, Defaults

import pytz


class Command(BaseCommand):
    def handle(self, *args, **options):
        defaults = Defaults(tzinfo=pytz.timezone('Europe/Moscow'))
        updater = Updater('token', defaults=defaults)

        updater.start_polling()
        updater.idle()
