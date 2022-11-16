from django.contrib import admin

from telegrambot.models import *


@admin.register(BotAnswer)
class BotAnswerAdmin(admin.ModelAdmin):
    search_fields = ('query',)
