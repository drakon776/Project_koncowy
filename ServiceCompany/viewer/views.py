from django.shortcuts import render
from django.views.generic import FormView
from viewer.forms import FaultForm


def user(request):
    return render(request, template_name='user.html')


class ViewFault(FormView):
    template_name = 'form.html'
    form_class = FaultForm
