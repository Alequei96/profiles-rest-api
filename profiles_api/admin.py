from django.contrib import admin

from profiles_api import models

#Makes accesible our custom models through Admin interface
admin.site.register(models.UserProfile)
