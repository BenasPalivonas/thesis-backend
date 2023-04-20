from django.contrib import admin

from core.models import Assignment, Lecture, LectureSubject, Lecturer, Student, StudentGroup

# Register your models here.
admin.site.register(Lecturer)
admin.site.register(LectureSubject)
admin.site.register(Assignment)
admin.site.register(Student)
admin.site.register(StudentGroup)


@admin.register(Lecture)
class MyModelAdmin(admin.ModelAdmin):
    # ...
    filter_horizontal = ['student_groups']
