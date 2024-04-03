from django import forms
from .models import Operators


class DateInput(forms.DateInput):
    input_type = "date"


class OperatorsForm(forms.ModelForm):
    name = forms.CharField(max_length=500)
    email = forms.EmailField(max_length=300)
    birth_date = forms.DateField(widget=DateInput())
    admission_date = forms.DateField(widget=DateInput())
    active = forms.BooleanField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True
        self.fields['birth_date'].required = True
        self.fields['admission_date'].required = True
        self.fields['active'].required = True

    class Meta:
        model = Operators
        fields = (
            'name',
            'email',
            'birth_date',
            'admission_date',
            'active',

        )

       