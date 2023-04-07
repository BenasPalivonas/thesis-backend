from django.contrib import admin

from core.models import Lecture, Lecturer, Student, StudentGroup

# Register your models here.
admin.site.register(Lecturer)
admin.site.register(Lecture)
admin.site.register(Student)
admin.site.register(StudentGroup)
