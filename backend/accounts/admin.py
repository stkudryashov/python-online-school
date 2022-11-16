from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import Group

from accounts.models import *


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Панель управления пользователями
    """

    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password', 'type')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'telegram_id')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'type')
        }),
        (_('Personal info'), {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name')
        }),
        ('Пароль', {
            'classes': ('wide',),
            'fields': ('password1', 'password2')
        })
    )

    list_display = ('email', 'first_name', 'last_name', 'type', 'is_staff')
    list_filter = ('type', 'is_active')

    ordering = ('date_joined',)


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    """
    Панель дополнительной информации о пользователях
    """

    list_display = ('user', 'date_of_birth', 'phone_number')


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    """
    Панель групп пользователей
    """

    list_display = ('title',)
    filter_horizontal = ('permissions',)


# Удаляем из панели стандартную модель групп
admin.site.unregister(Group)


@admin.register(UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
    """
    Панель прав доступа для пользователей определенной группы
    """

    list_display = ('title', 'permission')
