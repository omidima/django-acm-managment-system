from django.contrib import admin
from .models import GroupMedias, Group, News

# Register your models here.
admin.site.register(GroupMedias)
admin.site.register(News)
admin.site.register(Group)
