from django.http import JsonResponse
from django.views.generic import View
from ..models import Driver, Vehicle
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers
import json
import traceback
from dateutil import parser


class DriverViewAPI(View):

    def get(self,request, *args, **kwargs,):
        
        drivers = Driver.objects.all()
        
        if request.GET.get('created_at__gte') == '10-11-2021':
            date = parser.parse(('-'.join('10-11-2021'.split('-')[::-1])+' '+'00:00:00+00:00'))
            newDriver = list(Driver.objects.all())
            drivers = drivers.exclude(created_at__gte=date)
        
        elif request.GET.get('created_at__lte') == '16-11-2021':
            date = parser.parse(('-'.join('10-11-2021'.split('-')[::-1])+' '+'00:00:00+00:00'))
            newDriver = list(Driver.objects.all())
            drivers = drivers.exclude(created_at__gte=date)
           
        drivers = drivers.values('first_name','last_name','created_at','updated_at')   
        data = {
            'drivers' : list(drivers)
        }
        return JsonResponse(data)
    
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
        
        Driver.objects.filter(pk=id).delete()
        newDriver = Driver.objects.all()
        data = json.loads(serializers.serialize('json',[newDriver]))
          
        return JsonResponse({'success':data})

class VehicleViewAPI(View):
    
    def get(self,request, *args, **kwargs):
        vehicles = Vehicle.objects.all()

        if request.GET.get('with_drivers') == 'yes':
            vehicles = vehicles.exclude(driver_id__isnull=True)
        elif request.GET.get('with_drivers') == 'no':
            vehicles = vehicles.exclude(driver_id__isnull=False)
            
        vehicles = vehicles.values('driver_id','make','model','plate_number','created_at','updated_at')
        data = {
        'vehicles' : list(vehicles)
        }
        return JsonResponse(data)
    
    @method_decorator(csrf_exempt, name='dispatch')
    def post(self,request,*args, **kwargs):
        body = json.loads(request.body.decode("utf-8"))
        try:
            driver_instance = Driver.objects.get(pk=body['driver_id'])
            newCar = Vehicle.objects.create(driver_id=driver_instance,make=body['make'],model=body['model'],plate_number=body['plate_number'])
            data = json.loads(serializers.serialize('json',[newCar]))
        except Exception:
            return JsonResponse({"error":traceback.format_exc()})
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
        try:
            driver_instance = Driver.objects.get(pk=body['driver_id'])
            Vehicle.objects.filter(pk=id).update(driver_id=driver_instance,make=body['make'],model=body['model'],plate_number=body['plate_number'])
            newVehicle = Vehicle.objects.filter(pk=id)
            data = json.loads(serializers.serialize('json',[newVehicle]))
        except Exception:
            return JsonResponse({"error":traceback.format_exc()})
        return JsonResponse({'success':data})
    
    @method_decorator(csrf_exempt, name='dispatch')
    def delete(self,request,id, *args, **kwargs):
        Vehicle.objects.filter(pk=id).delete()     
        newVehicle = Vehicle.objects.all()
        try:
            data = json.loads(serializers.serialize('json',[newVehicle]))
        except Exception:
            return JsonResponse({"error":traceback.format_exc()})
        return JsonResponse({'success':data})

class VehicleViewAPISetDriver(View):

    @method_decorator(csrf_exempt, name='dispatch')
    def post(self,request,id,*args, **kwargs):
        body = json.loads(request.body.decode("utf-8"))
        try:
            driver_instance = Driver.objects.get(pk=body['driver_id'])
            oldOwner = Vehicle.objects.filter(pk=id).values('driver_id')
            newOwner= Vehicle.objects.filter(pk=id).update(driver_id=driver_instance)
            vehicles = Vehicle.objects.filter(pk=id).values('driver_id','make','model','plate_number','created_at','updated_at')
            data = {'New Owner' : list(vehicles),
            'Old Owner':list(oldOwner)}
        except Exception:
            return JsonResponse({"error":traceback.format_exc()})
        return JsonResponse({'success': data})