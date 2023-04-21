from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Assignment
from core.views import send_notification


@receiver(post_save, sender=Assignment)
def mymodel_created(sender, instance, created, **kwargs):
    if created:
        print('signals work')
        if instance.lecturer is not None:
            send_notification(instance.name, instance.details)
