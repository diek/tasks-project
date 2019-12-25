from django.urls import path

from . import views

urlpatterns = [
    path('reports', views.reporting, name='reports'),
]
