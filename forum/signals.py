from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from forum.models import Profile, Thread


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a profile when a user is created"""

    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Save a profile when a user is saved"""

    instance.profile.save()


@receiver(pre_save, sender=Thread)
def update_updated_on(sender, instance, **kwargs):
    """Set updated_on to now when the user is updated"""

    if instance.pk is not None:
        instance.updated_on = timezone.now()
