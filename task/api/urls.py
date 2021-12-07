from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import DriverViewAPI,DriverViewAPIWithID, VehicleViewAPIWithID, VehicleViewAPI

app_name = 'task-django'

urlpatterns = [
    path('drivers/driver/', csrf_exempt(DriverViewAPI.as_view()), name = 'driver.html'),
    path('drivers/driver/<int:id>/', DriverViewAPIWithID.as_view(), name = 'driver.html'),
    path('vehicles/vehicle/', VehicleViewAPI.as_view(), name = 'vehicle.html'),
    path('vehicles/vehicle/<int:id>/', VehicleViewAPIWithID.as_view(), name = 'vehicle.html'),
] 
