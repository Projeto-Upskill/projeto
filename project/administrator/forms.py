from django import forms
from .models import Administrator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
    input_type = "date"


class PasswordInput(forms.PasswordInput):
    input_type = 'password'


class AdministratorForm(forms.ModelForm):
    first_name = forms.CharField(max_length=500)
    last_name = forms.CharField(max_length=500)
    email = forms.EmailField(max_length=300)
    birth_date = forms.DateField(widget=DateInput())
    active = forms.BooleanField()
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'active',
            'username',
            'password'

        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].required = True
            self.fields['name'].required = True
            self.fields['birth_date'].required = True
            self.fields['active'].required = True
