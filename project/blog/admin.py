from django.contrib import admin
from . models import Projects, Tags,Profile,Messages,Skills

# Register your models here.

admin.site.register(Projects)
admin.site.register(Tags)
admin.site.register(Profile)
admin.site.register(Skills)
admin.site.register(Messages)
