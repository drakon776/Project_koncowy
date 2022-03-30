from django.urls import path
from .views import user, ViewFault, faults, faults_service, main_page

app_name = 'viewer'
urlpatterns = [
    path('', main_page, name="main_page"),
    path('fault/', ViewFault.as_view(), name='faulttype', ),
    path('faults/', faults),
    path('faults_service/', faults_service),
    path('user/', user),


]
