from django.contrib import admin
from django.urls import path, include
from viewer.models import Client, Service, FaultType
from viewer.views import user

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(FaultType)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('viewer.urls', namespace='viewer')),
    path('index/', user, name="index"),

]
