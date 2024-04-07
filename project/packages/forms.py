from django import forms
from .models import Package, PackageDiscount, PackageDiscountPackage, InvoicePackage
from customers.models import Customer

class PackageForm(forms.ModelForm):
    name = forms.CharField(max_length=500)
    active = forms.BooleanField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['active'].required = True
    
    class Meta:
        model = Package
        fields = (
            'name',
            'active',

        )
        
class PackageDiscountForm(forms.ModelForm):
    discount_rate = forms.DecimalField(max_digits=4, decimal_places=2)
    active = forms.BooleanField()
    id_package = forms.ModelChoiceField(queryset=Package.objects.all()) 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['discount_rate'].required = True
        self.fields['active'].required = True
        self.fields['id_package'].required = True
    
    class Meta:
        model = PackageDiscount
        fields = (
            'discount_rate',
            'active',
            'id_package',

        )
        

class PackageDiscountPackageForm(forms.ModelForm):
    id_package_discount = forms.ModelChoiceField(queryset=PackageDiscount.objects.all())
    id_package = forms.ModelChoiceField(queryset=Package.objects.all()) 
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_package_discount'].required = True
        self.fields['id_package'].required = True  
       
    class Meta:
        model = PackageDiscountPackage
        fields = ['id_package_discount_package', 'id_package', 'id_package_discount']
        labels = {
            'id_package_discount_package': 'Package_Discount_Package',
            'id_package': 'Package_ID',
            'id_package_discount': 'Package_Discount_ID',
        }


class InvoicePackageForm(forms.ModelForm):
    id_customer = forms.ModelChoiceField(queryset=Customer.objects.all())  
    id_package = forms.ModelChoiceField(queryset=Package.objects.all())
    final_package_price = forms.DecimalField(max_digits=10, decimal_places=2)
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_customer'].required = True
        self.fields['id_package'].required = True 
        self.fields['final_package_price'].required = True 
    
    class Meta:
        model = InvoicePackage
        fields = ['id_invoice_package', 'id_customer', 'id_package', 'final_package_price']
        labels = {
            'id_invoice_package': 'Invoice_Package_ID',
            'id_customer': 'Customer_ID',
            'id_package': 'Package_ID',
            'final_package_price': 'Final_Package_Price',
        }