from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils import timezone
from .validators import validate_plate_numberLATIN,validate_plate_numberCYRYLLIC

NOW = timezone.now()


class Driver(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=NOW)
    updated_at = models.DateTimeField(default=NOW)
    def __str__(self):
        return self.first_name      


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver,on_delete=SET_NULL,unique=True,null=True, blank=True)
    make = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    plate_number = models.CharField(max_length=10,validators = [validate_plate_numberLATIN,validate_plate_numberCYRYLLIC], unique=True)
    created_at = models.DateTimeField(default=NOW)
    updated_at = models.DateTimeField(default=NOW)
    def __str__(self):
        return self.make




