from django.forms import Form, ModelForm, CharField, Textarea, ChoiceField
from viewer.models import Client, FaultType


class UserForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        name = CharField()

class FaultFormModel(ModelForm):

    class Meta:
        model = FaultType
        fields = ('name', 'address', 'desc')

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
    address = ChoiceField(choices=(('1', 'Os.'), ('2', 'Ul.')))
    desc = CharField(widget=Textarea, required=False)
