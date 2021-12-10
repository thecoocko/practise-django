from django.contrib import admin
from django.db.models import fields
from .models import Driver, Vehicle
from django.forms.models import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField  


admin.site.register(Driver)
admin.site.register(Vehicle)






