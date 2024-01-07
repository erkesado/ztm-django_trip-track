from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(
        User, related_name='trips', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.city}'


class Note(models.Model):
    NOTE_TYPES = (
        ('event', 'Event'),
        ('dining', 'Dining'),
        ('experience', 'Experience'),
        ('general', 'General'),
    )

    trip = models.ForeignKey(Trip, related_name='notes',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=NOTE_TYPES)
    img = models.ImageField(upload_to='notes', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(
        default=1, validators=[MaxValueValidator(5)])

    def __str__(self) -> str:
        return f'{self.name} in {self.trip.city}'
