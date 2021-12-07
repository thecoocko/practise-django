from django.http import JsonResponse
from django.views.generic import View
from ..models import Driver, Vehicle
from django.forms import  modelform_factory
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class DriverViewAPI(View):
    
    def get(self,request, *args, **kwargs):
        drivers = Driver.objects.values('first_name','last_name','created_at','updated_at')
        data = {
            'drivers' : list(drivers)
        }
        return JsonResponse(data)
    
    @method_decorator(csrf_exempt, name='dispatch')
    def post(self,request,*args, **kwargs):
        return JsonResponse({'success':'post'})
    
    @method_decorator(csrf_exempt, name='dispatch')
    def put(self,request,*args, **kwargs):
        return JsonResponse({'success':"update"})
    
    @method_decorator(csrf_exempt, name='dispatch')
    def delete(self,request, *args, **kwargs):
        return JsonResponse({'success':"delete"})

@method_decorator(csrf_exempt, name='dispatch')
class VehicleViewAPI(View):
    pass