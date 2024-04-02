from django import forms
from .models import Administrator, User


class DateInput(forms.DateInput):
    input_type = "date"


class AdministratorForm(forms.ModelForm):
    first_name = forms.CharField(max_length=500)
    last_name = forms.CharField(max_length=500)
    email = forms.EmailField(max_length=300)
    birth_date = forms.DateField(widget=DateInput())
    active = forms.BooleanField()

    class Meta:
        model = Administrator
        fields = (
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'active',

        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].required = True
            self.fields['name'].required = True
            self.fields['birth_date'].required = True
            self.fields['active'].required = True
