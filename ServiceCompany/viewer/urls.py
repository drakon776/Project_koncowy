from django.urls import path
from .views import user, ViewFault, faults, faults_service

app_name = 'viewer'
urlpatterns = [
    path('faults/', faults),  # pokazuje liste usterek
    path('faults_service/', faults_service),
    path('', user, name="index"),
    path('fault/', ViewFault.as_view(), name='faulttype', ),

]
