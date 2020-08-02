from django.shortcuts import render
from django.contrib.auth.views import LoginView
from viewer.forms import SubmittableAuthenticationForm


def user(request):
    return render(request, template_name='user.html')


class SubmittableLoginView(LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'form.html'
