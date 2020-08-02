from django.forms import Form, ModelForm, CharField, ModelChoiceField, Textarea, ChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from django.contrib.auth.forms import UserCreationForm

from viewer.models import Client, Profile
from django.db.transaction import atomic


class UserForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        name = CharField()


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


class SubmittableForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))


class SignUpForm(SubmittableForm, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    telephone = CharField(widget=Textarea)

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        telephone = self.cleaned_data['telephone']
        profile = Profile(telephone=telephone, user=result)
        if commit:
            profile.save()
        return result
