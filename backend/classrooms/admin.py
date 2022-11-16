from django.contrib import admin

from classrooms.models import *


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'date_start', 'date_end', 'is_end')


@admin.register(StudentClassroom)
class StudentClassroomAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'student', 'is_completed')
    search_fields = ('classroom__title', 'student__email')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'classroom', 'teacher', 'date_of_lesson')


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('student', 'schedule', 'date_of_publication', 'is_accepted')
    search_fields = ('student__email',)
