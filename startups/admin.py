from django.contrib import admin
from startups.models import Notifications, Comments, Startups, StartupStatuses, StartupFiles

# Register your models here.

admin.site.register(Notifications)
admin.site.register(Comments)
admin.site.register(Startups)
admin.site.register(StartupFiles)
admin.site.register(StartupStatuses)
