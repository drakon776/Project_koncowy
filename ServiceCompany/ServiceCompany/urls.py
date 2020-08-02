from django.contrib import admin
from django.urls import path
from viewer.models import Client, Service
from viewer.views import user, SubmittableLoginView
from django.contrib.auth.views import LoginView
admin.site.register(Client)
admin.site.register(Service)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
]
