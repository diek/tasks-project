from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('<int:task_id>/', views.task, name='task'),
]
