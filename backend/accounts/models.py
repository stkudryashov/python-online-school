from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _

from django.core.validators import RegexValidator


class CustomUserManager(BaseUserManager):
    """
    Миксин для управления пользователями
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создать и сохранить пользователя с переданными email и password
        """

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Создание обычного пользователя
        """

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создание суперпользователя
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Модель пользователя платформы
    """

    email = models.EmailField(_('email address'), unique=True)

    # blank=True, null=True только через админ панель
    type = models.ForeignKey('UserType', on_delete=models.PROTECT, related_name='users',
                             verbose_name='тип', blank=True, null=True)

    telegram_id = models.CharField(max_length=16, blank=True, null=True, verbose_name='telegram ID')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    username = None

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('date_joined',)


class UserInfo(models.Model):
    """
    Дополнительная информация о пользователе
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info', verbose_name='пользователь')

    date_of_birth = models.DateField(blank=True, null=True, verbose_name='дата рождения')

    phone_number_regex = RegexValidator(regex=r'^((\+7|7|8)+([0-9]){10})$')
    phone_number = models.CharField(
        verbose_name='номер телефона',
        validators=[phone_number_regex],
        unique=True, blank=True, null=True,
        max_length=16
    )

    city = models.CharField(blank=True, null=True, max_length=32, verbose_name='город')
    about_me = models.TextField(blank=True, null=True, verbose_name='обо мне')

    def __str__(self):
        return f'{self.user.email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class UserType(models.Model):
    """
    Модель группы пользователей
    """

    title = models.CharField(max_length=32, verbose_name='название группы')
    permissions = models.ManyToManyField('UserPermission', verbose_name='права группы')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'тип пользователей'
        verbose_name_plural = 'типы пользователей'


class UserPermission(models.Model):
    """
    Модель прав доступа для пользователей определенной группы
    """

    permission = models.CharField(max_length=64, verbose_name='идентификатор')
    title = models.CharField(max_length=64, verbose_name='название')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'доступ'
        verbose_name_plural = 'права доступа'
