from django.db import models

from lessons.models import Module


class Course(models.Model):
    """
    Модель курса, который наполнен модулями из приложения lessons
    """

    title = models.CharField(max_length=64, verbose_name='название курса')
    description = models.TextField(verbose_name='описание курса')

    modules = models.ManyToManyField(Module, through='CourseModule', verbose_name='модули курса')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class CourseModule(models.Model):
    """
    Модули на курсе с порядковыми номерами
    """

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    module = models.ForeignKey(Module, on_delete=models.PROTECT, verbose_name='модуль')

    order_number = models.PositiveIntegerField(verbose_name='порядок модуля в курсе')

    def __str__(self):
        return f'{self.course.title} - {self.module.title} - {self.order_number}'

    class Meta:
        verbose_name = 'модуль курса'
        verbose_name_plural = 'модули курса'

        ordering = ['course', 'order_number']
