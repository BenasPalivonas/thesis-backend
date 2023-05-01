from django.contrib import admin

from core.models import Assignment, Venue, Lecture, LectureSubject, Lecturer, Student, StudentGroup

# Register your models here.
admin.site.register(Lecturer)
admin.site.register(LectureSubject)
admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Venue)


@admin.register(Assignment, Lecture)
class MyModelAdmin(admin.ModelAdmin):
    # ...
    filter_horizontal = ['student_groups']
