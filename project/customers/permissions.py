from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_customers_group(**kwargs):
    customer_group, created = Group.objects.get_or_create(name='customer_group')
    permissions = [
        Permission.objects.get(codename='view_service'),
        Permission.objects.get(codename='view_servicediscount'),
        Permission.objects.get(codename='view_servicetype'),
        Permission.objects.get(codename='view_invoiceservice'),
        Permission.objects.get(codename='view_customer'),
        Permission.objects.get(codename='view_address'),
        Permission.objects.get(codename='view_package'),
        Permission.objects.get(codename='view_packagediscount'),
        Permission.objects.get(codename='view_invoicepackage')
    ]
    # this next line is to delete all permissions if some are added that we dont want
    # customer_group.permissions.clear()
    for p in permissions:
        customer_group.permissions.add(p)


    return customer_group