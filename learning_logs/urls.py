"""Определяет схемы URL для learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('toics/<int:topic_id>/', views.topic, name='topic'),
    # Страница создания нового топика
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница создания нового комментария
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Редактирование записей (комментов)
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry')
]
