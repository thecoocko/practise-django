from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
import json


class DriverView (View):
    def get(self,request,*args, **kwargs):
        return render(request, template_name='drivers.html')

class VehicleView (View):
    def get(self,request,*args, **kwargs):
        return render(request, template_name='vehicles.html')



