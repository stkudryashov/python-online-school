from django.db import models

from accounts.models import User
from courses.models import Course
from lessons.models import Lesson


class Classroom(models.Model):
    """
    Модель учебной группы
    """

    title = models.CharField(max_length=32, verbose_name='название группы')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='classrooms', verbose_name='курс')

    date_start = models.DateField(blank=True, null=True, verbose_name='дата начала учебы')
    date_end = models.DateField(blank=True, null=True, verbose_name='дата завершения учебы')

    is_end = models.BooleanField(default=False, verbose_name='обучение закончено')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'учебная группа'
        verbose_name_plural = 'учебные группы'
        ordering = ('-date_end',)


class StudentClassroom(models.Model):
    """
    Учебная группа студента
    """

    student = models.ForeignKey(User, verbose_name='ученик', on_delete=models.PROTECT)
    classroom = models.ForeignKey(Classroom, verbose_name='группа', on_delete=models.PROTECT)

    is_completed = models.BooleanField(default=False, verbose_name='закончил обучение')

    class Meta:
        verbose_name = 'группа студента'
        verbose_name_plural = 'группы студентов'

        ordering = ['classroom']

        constraints = [
            models.UniqueConstraint(fields=['classroom', 'student'], name='unique_student_classroom'),
        ]


class Schedule(models.Model):
    """
    Расписание занятий
    """

    teacher = models.ForeignKey(User, verbose_name='преподаватель', on_delete=models.PROTECT)
    classroom = models.ForeignKey(Classroom, verbose_name='группа', on_delete=models.PROTECT, related_name='schedule')
    lesson = models.ForeignKey(Lesson, verbose_name='урок', on_delete=models.PROTECT)

    date_of_lesson = models.DateTimeField(verbose_name='дата проведения занятия')

    def __str__(self):
        return f'{self.lesson.title} - {self.classroom.title}'

    class Meta:
        verbose_name = 'занятие'
        verbose_name_plural = 'расписание занятий'

        ordering = ['-date_of_lesson']


class Homework(models.Model):
    """
    Домашнее задание ученика
    """

    url = models.URLField(verbose_name='ссылка на домашнее задание', max_length=256)
    student = models.ForeignKey(User, verbose_name='ученик', on_delete=models.CASCADE)

    schedule = models.ForeignKey(Schedule, verbose_name='урок', on_delete=models.CASCADE, related_name='homeworks')

    need_to_fix = models.BooleanField(default=False, verbose_name='требует доработки')
    is_accepted = models.BooleanField(default=False, verbose_name='работа выполнена верно')

    date_of_publication = models.DateTimeField(auto_now_add=True, verbose_name='дата сдачи работы')

    def __str__(self):
        return f'{self.schedule} - {self.student.email}'

    class Meta:
        verbose_name = 'домашнее задание'
        verbose_name_plural = 'домашние задания'

        constraints = [
            models.UniqueConstraint(fields=['student', 'schedule'], name='unique_student_schedule'),
        ]
