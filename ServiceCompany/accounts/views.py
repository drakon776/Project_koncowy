from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import SignUpForm, SubmittableAuthenticationForm, SubmittablePasswordChangeForm
from viewer.mixins import TitleMixin, SuccessMessagedFormMixin
from django.contrib.auth.views import LoginView, PasswordChangeView


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')


class UserLoginView(LoginView,TitleMixin, SuccessMessagedFormMixin,):
    title = 'Login'
    success_message = 'Successfully logged in!'
    template_name = 'form.html'
    form_class = SubmittableAuthenticationForm


class SubmitableUserPasswordChange(PasswordChangeView):
    form_class = SubmittablePasswordChangeForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')

