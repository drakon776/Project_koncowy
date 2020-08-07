from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import SignUpForm, SubmittableAuthenticationForm
from viewer.mixins import TitleMixin, SuccessMessagedFormMixin
from django.contrib.auth.views import LoginView


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')


class UserLoginView(LoginView,TitleMixin, SuccessMessagedFormMixin,):
    title = 'Login'
    success_message = 'Successfully logged in!'
    template_name = 'form.html'
    form_class = SubmittableAuthenticationForm