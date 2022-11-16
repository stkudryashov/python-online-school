from django.db import models


class BotAnswer(models.Model):
    """
    Ответы для Telegram бота
    """

    query = models.CharField(max_length=32, verbose_name='название запроса')
    text = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return f'{self.query}'

    class Meta:
        verbose_name = 'ответ бота'
        verbose_name_plural = 'ответы бота'
