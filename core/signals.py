from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Assignment, Lecturer
from core.views import send_notification
from django.contrib.auth.models import User, Group


@receiver(post_save, sender=Assignment)
def mymodel_created(sender, instance, created, **kwargs):
    if created:
        print('signals work')
        if instance.lecturer is not None:
            send_notification(instance.name, instance.details)


@receiver(post_save, sender=Lecturer)
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
