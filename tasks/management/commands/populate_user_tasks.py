import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.utils import timezone

from tasks.models import Task, UserTask


def generate_user_task():
    User = get_user_model()
    users = User.objects.values_list('pk', flat=True).order_by('pk')
    tasks = Task.objects.values_list('pk', flat=True).order_by('pk')

    user_id = random.choice(users)
    user = User.objects.get(id=user_id)

    task_id = random.choice(tasks)
    task = Task.objects.get(id=task_id)

    date_time = timezone.now()

    user_task = UserTask(user=user, task=task, created=date_time)
    user_task.save()


class Command(BaseCommand):
    help = 'Generates x number of usertasks'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of user_tasks to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        count = 0
        for i in range(total):
            try:
                generate_user_task()
            except IntegrityError:
                count += 1
        if count:
            print(f"{total - count } of {total} were created, the user task already existed.")
        else:
            print(f"All {total} tasks were created.")
