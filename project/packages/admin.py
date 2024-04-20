from django.contrib import admin
from .models import Package, PackageDiscount, PackageDiscountPackage, InvoicePackage, PackageCustomer


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['id_package', 'name', 'package_initial_price', 'service1', 'service2', 'service3', 'service4',
                    'active']


@admin.register(PackageDiscount)
class PackageDiscountAdmin(admin.ModelAdmin):
    list_display = ['id_package_discount', 'discount_rate', 'active', 'id_package']


@admin.register(PackageDiscountPackage)
class PackageDiscountPackageAdmin(admin.ModelAdmin):
    list_display = ['id_package_discount_package', 'id_package', 'id_package_discount']


@admin.register(PackageCustomer)
class PackageCustomer(admin.ModelAdmin):
    list_display = ["id_package_customer", "package", "customer", "user"]


@admin.register(InvoicePackage)
class InvoicePackageAdmin(admin.ModelAdmin):
    exclude = ('final_package_price',)
    list_display = ['id_invoice_package', 'id_customer', 'id_package', 'final_package_price']
