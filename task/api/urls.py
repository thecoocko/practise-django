from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import DriverViewAPI,DriverViewAPIWithID,  VehicleViewAPIWithID, VehicleViewAPI,VehicleViewAPISetDriver

app_name = 'task'

name_driver = 'driver.html'
name_vehicle = 'vehicle.html'

urlpatterns = [
    path('drivers/driver/', csrf_exempt(DriverViewAPI.as_view()), name = name_driver),
    path('drivers/driver/<int:id>/', csrf_exempt(DriverViewAPIWithID.as_view()), name = name_driver),
    path('vehicles/vehicle/', csrf_exempt(VehicleViewAPI.as_view()), name = name_vehicle),
    path('vehicles/vehicle/<int:id>/', csrf_exempt(VehicleViewAPIWithID.as_view()), name = name_vehicle),
    path('vehicles/set_driver/<int:id>/', csrf_exempt(VehicleViewAPISetDriver.as_view()), name = name_vehicle),
    #set_driver not done
] 
