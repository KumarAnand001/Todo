from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="list"),
    path('update-task/<str:pk>/', updateTask, name="update"),
    path('delete-task/<str:pk>/', deleteTask, name="delete")
]