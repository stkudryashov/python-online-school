from django.db import models


class Module(models.Model):
    """
    Модель учебных модулей, которыми можно наполнять различные курсы
    """

    title = models.CharField(max_length=64, verbose_name='название')
    description = models.TextField(verbose_name='описание модуля')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'


class Lesson(models.Model):
    """
    Модель уроков, из которых состоят модули
    """

    title = models.CharField(max_length=64, verbose_name='название')
    description = models.TextField(verbose_name='описание урока')

    document_url = models.URLField(max_length=128, verbose_name='ссылка на документ')
    homework_url = models.URLField(max_length=128, verbose_name='ссылка на домашнее задание')

    module = models.ForeignKey(Module, on_delete=models.PROTECT, related_name='lessons', verbose_name='модуль')
    order_number = models.PositiveIntegerField(verbose_name='порядок урока в модуле')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ['module', 'order_number']

        constraints = [
            models.UniqueConstraint(fields=['module_id', 'order_number'], name='unique_module_order'),
        ]
