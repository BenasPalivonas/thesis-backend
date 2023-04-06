from django.contrib import admin

from core.models import Lecture, Lecturer

# Register your models here.
admin.site.register(Lecturer)
admin.site.register(Lecture)
