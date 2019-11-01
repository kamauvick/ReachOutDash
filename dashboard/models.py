from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    ROLES = (
        ('Doc', 'Doctor'),
        ('Sur', 'Surgeon'),
        ('Nur', 'Nurse'),
    )
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')
    profile_pic = models.ImageField(upload_to='dash_profile_pics/', blank=True, default='prof.jpg')
    contact = models.CharField(max_length=250)
    hospital = models.CharField(max_length=250)
    role = models.CharField(choices=ROLES, max_length=200)

    class Meta:
        db_table = 'dash_profiles'
        ordering = ['name']

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def search_profiles(cls, searchTerm):
        profiles = cls.objects.filter(name__icontains=searchTerm)
        return profiles

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(name=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.admin.save()
