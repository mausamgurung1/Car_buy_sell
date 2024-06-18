from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Location, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_user_location(sender, instance, created, **kwargs):
    if created:
        profile_location = Location.objects.create()
        Profile.objects.filter(pk=instance.pk).update(location=profile_location)

@receiver(post_delete, sender=Profile)
def profile_delete_location(sender, instance, **kwargs):
    if instance.location:
        instance.location.delete()
