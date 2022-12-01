from django.contrib import admin

from classrooms.models import Classroom, StudentClassroom, Schedule, Homework


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    """
    Панель учебных групп
    """

    list_display = ('title', 'course', 'date_start', 'date_end', 'is_end')


@admin.register(StudentClassroom)
class StudentClassroomAdmin(admin.ModelAdmin):
    """
    Панель учебных групп студентов
    """

    list_display = ('classroom', 'student', 'is_completed')
    search_fields = ('classroom__title', 'student__email')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """
    Панель расписания занятий
    """

    list_display = ('lesson', 'classroom', 'teacher', 'date_of_lesson')


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    """
    Панель домашних заданий
    """

    list_display = ('student', 'schedule', 'date_of_publication', 'is_accepted')
    search_fields = ('student__email',)
