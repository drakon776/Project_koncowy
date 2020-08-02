from django.contrib import admin
from django.urls import path
from viewer.models import Client, Service, FaultType
from viewer.views import user, ViewFault

from viewer.views import SignUpView

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(FaultType)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user, name="index"),
    path('fault/', ViewFault.as_view(), name='faulttype'),
    path('sign-up/',SignUpView.as_view(), name='sign-up')
]
