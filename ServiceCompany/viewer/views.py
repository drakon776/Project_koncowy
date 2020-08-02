from django.shortcuts import render
from django.views.generic import FormView

from django.views.generic import CreateView

from viewer.forms import FaultForm


def user(request):
    return render(request, template_name='user.html')


class ViewFault(FormView):
    template_name = 'form.html'
    form_class = FaultForm
#
#
# class SignUpView(CreateView):
#     title = 'Sign Up'
#     success_message = 'Successfully signed up!'
#     template_name = 'form.html'
