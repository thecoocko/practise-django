from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url 

urlpatterns = [
    url(r'^', include('task-django.api.urls')),
    path('admin/', admin.site.urls),
]