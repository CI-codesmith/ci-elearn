from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Role

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        # Assign default role 'Student' if it exists
        student_role, _ = Role.objects.get_or_create(name='Student', defaults={'description': 'Default student role'})
        profile.roles.add(student_role)
        profile.save()
