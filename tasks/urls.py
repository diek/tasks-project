from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('<int:task_id>/', views.task, name='task'),

    path('users-tasks/', views.users_tasks, name='users_tasks'),
    path('user-tasks/<int:user_id>/', views.user_tasks, name='user_tasks'),
]
