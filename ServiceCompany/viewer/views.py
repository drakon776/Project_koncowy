from django.shortcuts import render
from django.views.generic import FormView
from viewer.forms import FaultForm, FaultFormModel
from viewer.models import FaultType
from django.urls import reverse_lazy

def user(request):
    return render(request, template_name='user.html')


class ViewFault(FormView):
    template_name = 'form.html'
    form_class = FaultFormModel
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        fault = form.save(commit=False)
        fault.user = self.request.user
        fault.save()
        return super().form_valid(form)


def faults(request):
    return render(
        request, template_name='fault_view.html',
        context={'faults': FaultType.objects.all()}
    )
