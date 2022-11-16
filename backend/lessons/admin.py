from django.contrib import admin

from lessons.models import *


class ModuleLessonsInline(admin.StackedInline):
    model = Lesson
    extra = 0
    verbose_name_plural = 'список уроков в модуле'


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (ModuleLessonsInline,)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'order_number')
