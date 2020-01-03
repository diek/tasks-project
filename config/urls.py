from django.conf import settings
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'Tasks Admin Panel'
admin.site.site_title = 'Tasks - Admin'

urlpatterns = [
    path('tasks/', include('tasks.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
