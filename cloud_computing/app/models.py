from django.db import models
from django.utils import timezone


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    date_made = models.DateTimeField(default=timezone.now)
    healthy = models.BooleanField(default=False)


class Counter(models.Model):
    counter_field = models.PositiveIntegerField(default=0)
