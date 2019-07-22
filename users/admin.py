from django.contrib import admin
from users.models import Users, UserProfiles

# Register your models here.
admin.site.register(Users)
admin.site.register(UserProfiles)