from django.contrib import admin
from django.urls import path, include
from viewer.models import Client, Service, FaultType
from viewer.views import user, main_page

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(FaultType)

urlpatterns = [
    path('', include('viewer.urls', namespace='viewer')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('index/', user, name="index"),
    path('main/', main_page, name="main"),

]
