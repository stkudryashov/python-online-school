from django.contrib import admin

from telegrambot.models import BotAnswer


@admin.register(BotAnswer)
class BotAnswerAdmin(admin.ModelAdmin):
    """
    Панель ответов Telegram бота
    """

    search_fields = ('query',)
