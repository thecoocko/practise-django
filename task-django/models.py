from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

class Driver(models.Model):
    first_name = models.CharField(max_length=250,unique = True)
    last_name = models.CharField(max_length=250,unique = True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.first_name


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver,on_delete=CASCADE)
    make = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    plate_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.make




