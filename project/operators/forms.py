from django import forms
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = "date"


class PasswordInput(forms.PasswordInput):
    input_type = 'password'


class OperatorsForm(forms.ModelForm):
    first_name = forms.CharField(max_length=500)
    last_name = forms.CharField(max_length=500)
    email = forms.EmailField(max_length=300)
    birth_date = forms.DateField(widget=DateInput())
    admission_date = forms.DateField(widget=DateInput())
    active = forms.BooleanField()
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['birth_date'].required = True
        self.fields['admission_date'].required = True
        self.fields['active'].required = True

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'admission_date',
            'active',
            'username',
            'password'

        )

       