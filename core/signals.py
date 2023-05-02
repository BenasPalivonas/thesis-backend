from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from core.models import Assignment, Grade, Lecture, LectureSubject, Lecturer
from core.serializers import AssignmentSerializer
from core.views import send_notification
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate


@receiver(post_save, sender=Assignment)
def mymodel_created(sender, instance, created, **kwargs):
    if instance.name is not None:
        send_notification(instance, created, is_grade=False,
                          assignment_id=instance.id)


@receiver(post_save, sender=Grade)
def mymodel_created(sender, instance, created, **kwargs):
    if instance.grade is not None:
        send_notification(instance, created, is_grade=True,
                          assignment_id=instance.assignment.id)


def create_group(sender, **kwargs):
    group, created = Group.objects.get_or_create(name='destytojas')
    if created:
        content_type_assignment = ContentType.objects.get_for_model(Assignment)
        content_type_lecture = ContentType.objects.get_for_model(Lecture)
        content_type_lecture_subject = ContentType.objects.get_for_model(
            LectureSubject)

        add_perm_assignment = Permission.objects.get(
            codename='add_assignment', content_type=content_type_assignment)
        change_perm_assignment = Permission.objects.get(
            codename='change_assignment', content_type=content_type_assignment)
        delete_perm_assignment = Permission.objects.get(
            codename='delete_assignment', content_type=content_type_assignment)
        view_perm_assignment = Permission.objects.get(
            codename='view_assignment', content_type=content_type_assignment)

        add_perm_lecture = Permission.objects.get(
            codename='add_lecture', content_type=content_type_lecture)
        change_perm_lecture = Permission.objects.get(
            codename='change_lecture', content_type=content_type_lecture)
        delete_perm_lecture = Permission.objects.get(
            codename='delete_lecture', content_type=content_type_lecture)
        view_perm_lecture = Permission.objects.get(
            codename='view_lecture', content_type=content_type_lecture)

        add_perm_lecture_subject = Permission.objects.get(
            codename='add_lecture_subject', content_type=content_type_lecture_subject)
        change_perm_lecture_subject = Permission.objects.get(
            codename='change_lecture_subject', content_type=content_type_lecture_subject)
        delete_perm_lecture_subject = Permission.objects.get(
            codename='delete_lecture_subject', content_type=content_type_lecture_subject)
        view_perm_lecture_subject = Permission.objects.get(
            codename='view_lecture_subject', content_type=content_type_lecture_subject)

        group.permissions.add(add_perm_assignment, change_perm_assignment,
                              delete_perm_assignment, view_perm_assignment, add_perm_lecture, add_perm_lecture_subject, change_perm_lecture, change_perm_lecture_subject,
                              delete_perm_lecture, delete_perm_lecture_subject, view_perm_lecture, view_perm_lecture_subject)


@ receiver(post_save, sender=Lecturer)
def mymodel_created(sender, instance, created, **kwargs):
    if created:
        print('signals work')
        if instance.email is not None:
            user = User.objects.create_user(
                username=instance.email, email=instance.email)
            user.set_password(instance.password)
            user.is_staff = True
            group_name = 'destytojas'
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            user.save()
