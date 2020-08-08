from django.contrib import admin
from django.urls import path, include
from viewer.models import Client, Service, FaultType
from viewer.views import user, ViewFault,faults

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(FaultType)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user, name="index"),
    path('fault/', ViewFault.as_view(), name='faulttype',),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('faults/', faults) # pokazuje liste usterek


]
