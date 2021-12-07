from django.urls import path
from .views import DriverViewAPI, VehicleViewAPI

app_name = 'task-django'

urlpatterns = [
    path('drivers/driver/', DriverViewAPI.as_view(), name = 'driver.html'),
    path('drivers/', DriverViewAPI.as_view(), name = 'driver.html'),
    path('drivers/', DriverViewAPI.as_view(), name = 'driver.html'),
    path('drivers/', DriverViewAPI.as_view(), name = 'driver.html'),
    path('drivers/', DriverViewAPI.as_view(), name = 'driver.html'),
    path('drivers/', DriverViewAPI.as_view(), name = 'driver.html'),
    path('drivers/', DriverViewAPI.as_view(), name = 'driver.html'),
    path('vehicles/', VehicleViewAPI.as_view(), name = 'vehicle.html'),
    path('vehicles/', VehicleViewAPI.as_view(), name = 'vehicle.html'),
    path('vehicles/', VehicleViewAPI.as_view(), name = 'vehicle.html'),
    path('vehicles/', VehicleViewAPI.as_view(), name = 'vehicle.html'),
    path('vehicles/', VehicleViewAPI.as_view(), name = 'vehicle.html'),
    path('vehicles/', VehicleViewAPI.as_view(), name = 'vehicle.html'),
    path('vehicles/', VehicleViewAPI.as_view(), name = 'vehicle.html'),
] 
