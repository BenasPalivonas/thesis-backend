from django.contrib import admin
from django.utils.translation import gettext as _
from django.contrib.messages import SUCCESS

from core.models import Assignment, Grade, Venue, Lecture, LectureSubject, Lecturer, Student, StudentGroup

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


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'assignment', 'grade']
    list_filter = ['student', 'assignment']

    def save_model(self, request, obj, form, change):
        message = ''
        if Grade.objects.filter(student=obj.student, assignment=obj.assignment).exists():
            existing_grade = Grade.objects.get(
                student=obj.student, assignment=obj.assignment)
            existing_grade.grade = obj.grade
            existing_grade.save()
            if change is False:
                message = _("Since the student was already graded for this assignment, the grade for student %(student)s on assignment %(assignment)s has been updated.") % {
                    'student': existing_grade.student.username,
                    'assignment': existing_grade.assignment,
                }
        else:
            obj.save()
        self.message_user(request, message, SUCCESS)
