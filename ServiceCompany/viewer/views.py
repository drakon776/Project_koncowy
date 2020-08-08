from django.shortcuts import render
from django.views.generic import FormView
from viewer.forms import FaultForm, FaultFormModel
from viewer.models import FaultType
from django.urls import reverse_lazy

def user(request):
    return render(request, template_name='user.html')


# class SubmittableForm(Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))

# class ViewFault(FormView):
#     template_name = 'form.html'
#     form_class = FaultForm


class ViewFault(FormView):
    template_name = 'form.html'
    form_class = FaultFormModel
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def faults(request):
    return render(
        request, template_name='fault_view.html',
        context={'faults': FaultType.objects.all()}
    )

class FaultAdd(FormView):
    pass