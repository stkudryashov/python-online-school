from django.contrib import admin

from courses.models import *


class CourseModulesInline(admin.StackedInline):
    model = CourseModule
    extra = 0
    verbose_name_plural = 'список модулей в курсе'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (CourseModulesInline,)


@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
    list_display = ('course', 'module', 'order_number')
