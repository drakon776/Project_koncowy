from django.forms import Form, ModelForm, CharField


from viewer.models import Client

class UserForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
    name = CharField()


