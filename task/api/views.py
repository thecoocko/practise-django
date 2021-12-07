from django.http import JsonResponse
from django.views.generic import View
from ..models import Driver, Vehicle
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers
import json


class DriverViewAPI(View):
    
    def get(self,request, *args, **kwargs,):
        
        drivers = Driver.objects.values('first_name','last_name','created_at','updated_at')
        data = {
            'drivers' : list(drivers)
        }
        return JsonResponse({'success':data})
    
    @csrf_exempt
    def post(self,request,*args, **kwargs):
        body = json.loads(request.body.decode("utf-8"))
        newDriver = Driver.objects.create(first_name=body['first_name'],last_name=body['last_name'])
        data = json.loads(serializers.serialize('json',[newDriver]))
        return JsonResponse({'success':data})
    

class DriverViewAPIWithID(View):
    
    def get(self,request,id, *args, **kwargs,):
        
        drivers = Driver.objects.filter(pk=id).values('first_name','last_name','created_at','updated_at')
        data = {
            'drivers' : list(drivers)
        }
        return JsonResponse(data)

    @method_decorator(csrf_exempt, name='dispatch')
    def put(self,request,id,*args, **kwargs):
        body = json.loads(request.body.decode("utf-8"))
        Driver.objects.filter(pk=id).update(first_name=body['first_name'],last_name=body['last_name'])
        newDriver = Driver.objects.filter(pk=id)
        data = json.loads(serializers.serialize('json',[newDriver]))
        return JsonResponse({'success':data})
    
    @method_decorator(csrf_exempt, name='dispatch')
    def delete(self,request,id, *args, **kwargs):
        body = json.loads(request.body("utf-8"))
        Driver.objects.filter(pk=id).delete()
        newDriver = Driver.objects.all()
        data = json.loads(serializers.serialize('json',[newDriver]))
        return JsonResponse({'success':data})



class VehicleViewAPI(View):
    
    def get(self,request, *args, **kwargs):
        vehicles = Vehicle.objects.values('driver_id','make','model','plate_number','created_at','updated_at')
        data = {
            'drivers' : list(vehicles)
        }
        return JsonResponse(data)
    
    @method_decorator(csrf_exempt, name='dispatch')
    def post(self,request,*args, **kwargs):
        body = json.loads(request.body.decode("utf-8"))
        newCar = Vehicle.objects.create(driver_id=body['driver_id'],make=body['make'],model=body['mamodelke'],plate_number=body['plate_number'])
        data = json.loads(serializers.serialize('json',[newCar]))
        return JsonResponse({'success':data})
    


class VehicleViewAPIWithID(View):
    
    def get(self,request,id, *args, **kwargs):
        vehicles = Vehicle.objects.filter(pk=id).values('driver_id','make','model','plate_number','created_at','updated_at')
        data = {
            'vehicles' : list(vehicles)
        }
        return JsonResponse(data)
      
    @method_decorator(csrf_exempt, name='dispatch')
    def put(self,request,id,*args, **kwargs):
        body = json.loads(request.body.decode("utf-8"))
        Vehicle.objects.filter(pk=id).update(driver_id=body['driver_id'],make=body['make'],model=body['mamodelke'],plate_number=body['plate_number'])
        newVehicle = Vehicle.objects.filter(pk=id)
        data = json.loads(serializers.serialize('json',[newVehicle]))
        return JsonResponse({'success':data})
    
    @method_decorator(csrf_exempt, name='dispatch')
    def delete(self,request, *args, **kwargs):
        body = json.loads(request.body("utf-8"))
        Vehicle.objects.filter(pk=id).delete()
        newVehicle = Vehicle.objects.all()
        data = json.loads(serializers.serialize('json',[newVehicle]))
        return JsonResponse({'success':data})