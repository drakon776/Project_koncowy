from django.urls import path
from accounts.views import UserLoginView, SignUpView, SubmitableUserPasswordChange
from django.contrib.auth.views import LogoutView

app_name = 'accounts'
urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('change_password/', SubmitableUserPasswordChange.as_view(), name='change_password'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
