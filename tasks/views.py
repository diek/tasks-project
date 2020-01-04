from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Task, UserTask


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


def tasks(request):
    all_tasks = Task.objects.order_by('-task')
    return render(request, 'tasks/tasks.html', {'all_tasks': all_tasks})


def task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'tasks/task.html', {'task': task})


def users_tasks(request):
    users_tasks = UserTask.objects.order_by('-user')
    return render(request, 'tasks/users_tasks.html', {'users_tasks': users_tasks})
