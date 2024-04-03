#from django import forms
#from .models import Package

#class PackageForm(forms.ModelForm):
#    name = forms.CharField(max_length=500)
#    active = forms.BooleanField()
#    
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['name'].required = True
#        self.fields['active'].required = True
    
#    class Meta:
#        model = Package
#        fields = (
#            'name',
#            'active',

#        )
        
#class PackageDiscountForm(forms.ModelForm):
#    discount_rate = forms.DecimalField(max_digits=4, decimal_places=2)
#    active = forms.BooleanField()
#    id_package = forms.ModelChoiceField(queryset=Package.objects.all()) 
    
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['discount_rate'].required = True
#        self.fields['active'].required = True
#        self.fields['id_package'].required = True
    
#    class Meta:
#        model = Package
#        fields = (
#            'discount_rate',
#            'active',
#            'id_package',

#        )
        

