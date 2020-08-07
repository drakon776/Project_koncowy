from django.forms import Form, CharField, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.db.transaction import atomic
from viewer.models import Profile


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


class SubmittableAuthenticationForm(SubmittableForm, AuthenticationForm):
    pass

class SubmittablePasswordChangeForm(SubmittableForm, PasswordChangeForm):
    pass
