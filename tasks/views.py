from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Task


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


def tasks(request):
    all_tasks = Task.objects.order_by('-created')
    return render(request, 'tasks/tasks.html', {'all_tasks': all_tasks})


def task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'tasks/task.html', {'task': task})
