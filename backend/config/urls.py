"""
Python Online School URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/courses/', include('courses.urls')),
]

admin.site.site_header = 'Python Online School'
admin.site.site_title = 'Python Online School'
