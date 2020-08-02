from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from django.views.generic import CreateView

from viewer.forms import FaultForm, SignUpForm


def user(request):
    return render(request, template_name='user.html')


class ViewFault(FormView):
    template_name = 'form.html'
    form_class = FaultForm


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')