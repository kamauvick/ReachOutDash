from django.contrib.auth.models import User
from django.db import models


class Chv(models.Model):
    name = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile')
    age = models.IntegerField()
    phonenumber = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='chv_profiles/', blank=True, default='prof.jpg')
    location = models.CharField(max_length=200)

    class Meta:
        db_table = 'chv'
        ordering = ['-name']

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def get_all_chvs(cls):
        chvs = cls.objects.all()
        return chvs
    #
    # @receiver(post_save, sender=User)
    # def create_chv(sender, instance, created, **kwargs):
    #     if created:
    #         Chv.objects.create(name=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_chv(sender, instance, **kwargs):
    #     instance.profile.save()


class Patient(models.Model):
    URGENCY_LEVELS = (
        ('red', 'High severity'),
        ('yellow', 'Moderate severity'),
        ('green', 'Low severity'),
        ('blue', 'Unknown severity'),
    )
    LOCATIONS = (
        ('Juja', 'Gachororo'),
        ('High Point', 'Sewage'), 
        ('K-road', 'Stage'),
        ('Gwa-Kairu', 'Estate'),
        ('Ruiru', 'Kimbo')
    )
    name = models.CharField(max_length=255)
    examiner = models.ForeignKey('Chv', on_delete=models.CASCADE, related_name='chv')
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    location = models.CharField(choices=LOCATIONS, max_length=200, default='Ruiru')
    time = models.DateTimeField()
    symptoms = models.TextField()
    urgency = models.CharField(max_length=200, choices=URGENCY_LEVELS, default='blue')
    action_taken = models.TextField()

    class Meta:
        db_table = 'patient'
        ordering = ['-name']

    def __str__(self):
        return f'{self.name},::: {self.location}'

    @classmethod
    def get_all_patients(cls):
        patients = cls.objects.all()
        return patients


class Emergencies(models.Model):
    Emergency_TYPES = (
        ('Road', 'Road accidents'),
        ('Fire', 'Fire emergencies'),
        ('Water', 'Water related accidents'),
        ('Sickness', 'Sick people emergencies'),
    )
    type = models.CharField(max_length=200, choices=Emergency_TYPES, default='Sickness')
    location = models.ForeignKey('Emergencies', on_delete=models.CASCADE, related_name='locale')
    reported_by = models.ForeignKey('Chv', on_delete=models.CASCADE, related_name='reporter')

    class Meta:
        db_table = 'emergencies'
        ordering = ['type']

    @classmethod
    def get_all_emergencies(cls):
        emergencies = cls.objects.all()
        return emergencies


class Location(models.Model):
    ROAD_ACCESS = (
        ('Great', 'The roads are well passable in all weather conditions'),
        ('Good', 'The roads are passable in favourable weather conditions'),
        ('Bad', 'The roads are not passable'),
    )
    name = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    accessibility = models.CharField(max_length=200, choices=ROAD_ACCESS)

    class Meta:
        db_table = 'location'
        ordering = ['-name']

    @classmethod
    def get_all_locations(cls):
        locations = cls.objects.all()
        return locations
