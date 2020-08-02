from django.contrib import admin
from django.urls import path
from viewer.models import Client, Service, FaultType
from viewer.views import user, ViewFault

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(FaultType)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user),
    path('fault/', ViewFault.as_view(), name='faulttype')
]
