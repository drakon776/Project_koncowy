from django.forms import Form, ModelForm, CharField, Textarea, ChoiceField, Field, TextInput,IntegerField
from viewer.models import Client, FaultType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class SubmittableForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))


class UserForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        name = CharField()


class FaultFormModel(ModelForm):
    class Meta:
        model = FaultType
        fields = ('name', 'address', 'phone', 'desc')


    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'



class FaultForm(Form):
    fault_types = (
        ("1", "Domofon"),
        ("2", "CCTV"),
        ("3", "Alarm"),
        ("4", "Telewizja"),
        ("5", "C.O."),
        ("6", "C.W."),
        ("7", "Prace ślusarskie"),
        ("8", "Prace Hydrauliczne"),
    )
    name = ChoiceField(choices=fault_types)
    address = Field()
    desc = CharField(widget=Textarea, required=False)
    phone = IntegerField(max_value=12)

class ServiceView(Form):
    pass