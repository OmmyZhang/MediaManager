from django.contrib import admin
from .models import FileToTag,StTag,StFile
# Register your models here.

admin.site.register(FileToTag)
admin.site.register(StTag)
admin.site.register(StFile)
