from django.urls import path

from . import views

urlpatterns = [
    path('reports', views.tasks, name='tasks'),
]
