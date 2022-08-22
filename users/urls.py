"""Определяет схемы URL для users."""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Авторизация по умолчанию
    path('', include('django.contrib.auth.urls')),
]
