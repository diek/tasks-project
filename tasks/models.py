from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone_number = PhoneNumberField(default="+19020000000")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    task = models.CharField(max_length=50)
    notes = models.TextField()
    created_at = models.DateTimeField(
        verbose_name=u"Created at",
        auto_now_add=True
    )
    edited_by = models.ForeignKey(
        "CustomUser", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse("task_detail", args=[str(self.id)])


class UserTask(models.Model):
    user = models.ForeignKey(
        "CustomUser", related_name="user_tasks", on_delete=models.SET_NULL, null=True
    )
    task = models.ForeignKey(
        "Task", related_name="user_tasks", on_delete=models.SET_NULL, null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'task'], name='unique_user_task')
            ]
