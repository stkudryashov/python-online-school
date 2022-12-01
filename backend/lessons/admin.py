from django.contrib import admin

from lessons.models import Lesson, Module


class ModuleLessonsInline(admin.StackedInline):
    """
    Inline для уроков в модуле
    """

    model = Lesson
    extra = 0
    verbose_name_plural = 'список уроков в модуле'


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    """
    Панель модулей
    """

    list_display = ('title',)
    inlines = (ModuleLessonsInline,)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Панель уроков
    """

    list_display = ('title', 'module', 'order_number')
