from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Task, UserTask


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "phone_number",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "phone_number",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "is_staff",
                    "is_active",
                    "phone_number",
                ),
            },
        ),
    )
    search_fields = ("email", 'last_name')
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)


class TaskAdmin(admin.ModelAdmin):
    fields = ["task", "notes", "created_at", "edited_by"]
    list_display = ("task", "notes", "created_at", "edited_by")


admin.site.register(Task, TaskAdmin)


class UserTaskAdmin(admin.ModelAdmin):
    fields = ["task", "user", "created", "completed"]
    readonly_fields = ("created",)
    list_display = ("task", "user", "created", "completed")


admin.site.register(UserTask, UserTaskAdmin)
