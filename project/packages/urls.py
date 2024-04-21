from django.urls import path
from .views import PackageListView, PackageCreateView, PackageUpdateView, PackageDeleteView
from .views import PackageDiscountListView, PackageDiscountCreateView, PackageDiscountUpdateView, PackageDiscountDeleteView
from .views import PackageDiscountPackageListView, PackageDiscountPackageCreateView, PackageDiscountPackageUpdateView, PackageDiscountPackageDeleteView
from .views import InvoicePackageListView, InvoicePackageCreateView, InvoicePackageDeleteView, InvoicePackageUpdateView
from .views import PackageCustomerListView, PackageCustomerCreateView, PackageCustomerUpdateView, PackageCustomerDeleteView

app_name = 'packages'

urlpatterns = [
    #for package
    path('list', PackageListView.as_view(), name='package_list'), #read
    path('new', PackageCreateView.as_view(), name='package_create'),  # create
    path('<int:id_package>/edit', PackageUpdateView.as_view(), name='package_update'), #update
    path('<int:id_package>/delete', PackageDeleteView.as_view(), name='package_delete'), #delete
    #for package-discount
    path('package-discount/', PackageDiscountListView.as_view(), name='package_discount_list'), #read
    path('package-discount/new/', PackageDiscountCreateView.as_view(), name='package_discount_create'), #create
    path('package-discount/<int:id_package_discount>/edit/', PackageDiscountUpdateView.as_view(), name='package_discount_update'), #update
    path('package-discount/<int:id_package_discount>/delete/', PackageDiscountDeleteView.as_view(), name='package_discount_delete'), #delete
    #for package-discount-package
    path('package-discount-package/', PackageDiscountPackageListView.as_view(), name='package_discount_package_list'), #read
    path('package-discount-package/new/', PackageDiscountPackageCreateView.as_view(), name='package_discount_package_create'), #create
    path('package-discount-package/<int:id_package_discount_package>/edit/', PackageDiscountPackageUpdateView.as_view(), name='package_discount_package_update'), #update
    path('package-discount-package/<int:id_package_discount_package>/delete/', PackageDiscountPackageDeleteView.as_view(), name='package_discount_package_delete'), #delete
    #for invoice-package
    path('invoice-package/', InvoicePackageListView.as_view(), name='invoice_package_list'), #read
    path('invoice-package/new/', InvoicePackageCreateView.as_view(), name='invoice_package_create'), #create
    path('invoice-package/<int:id_invoice_package>/edit/', InvoicePackageUpdateView.as_view(), name='invoice_package_update'), #update
    path('invoice-package/<int:id_invoice_package>/delete/', InvoicePackageDeleteView.as_view(), name='invoice_package_delete'), #delete
    path("package_customer", PackageCustomerListView.as_view(), name="package_customer"),
    path("package_customer/create", PackageCustomerCreateView.as_view(), name="package_customer_create"),
    path("package_customer/<int:id_package_customer>/update", PackageCustomerUpdateView.as_view(), name="package_customer_update"),
    path("package_customer/<int:id_package_customer>/delete", PackageCustomerDeleteView.as_view(), name="package_customer_delete")
]