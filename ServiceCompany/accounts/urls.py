from django.urls import path
from accounts.views import UserLoginView, SignUpView

app_name = 'accounts'
urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('login/', UserLoginView.as_view(), name='login')

]
