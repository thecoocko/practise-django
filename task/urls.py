from django.urls import path
from .views import DriverView, VehicleView

app_name = 'task'

urlpatterns = [
    path('drivers/driver/', DriverView.as_view(), name = 'driver.html'),
    path('vehicles/vehicle/', VehicleView.as_view(), name = 'vehicle.html'),
] 
