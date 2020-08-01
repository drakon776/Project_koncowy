from django.contrib import admin
from django.urls import path

from viewer.models import Client, Service


admin.site.register(Client)
admin.site.register(Service)

urlpatterns = [
    path('admin/', admin.site.urls),
]
