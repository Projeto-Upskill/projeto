from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_operators_group(**kwargs):
    administrator_group, created = Group.objects.get_or_create(name='administrator_group')
    permissions = [
        Permission.objects.get(codename='add_user'),
        Permission.objects.get(codename='view_user'),
        Permission.objects.get(codename='change_user'),
        Permission.objects.get(codename='delete_user'),
        Permission.objects.get(codename='add_operators'),
        Permission.objects.get(codename='view_operators'),
        Permission.objects.get(codename='change_operators'),
        Permission.objects.get(codename='delete_operators'),
        Permission.objects.get(codename='add_service'),
        Permission.objects.get(codename='change_service'),
        Permission.objects.get(codename='view_service'),
        Permission.objects.get(codename='delete_service'),
        Permission.objects.get(codename='add_servicediscount'),
        Permission.objects.get(codename='change_servicediscount'),
        Permission.objects.get(codename='view_servicediscount'),
        Permission.objects.get(codename='delete_servicediscount'),
        Permission.objects.get(codename='add_servicetype'),
        Permission.objects.get(codename='change_servicetype'),
        Permission.objects.get(codename='view_servicetype'),
        Permission.objects.get(codename='delete_servicetype'),
        Permission.objects.get(codename='add_servicediscountservice'),
        Permission.objects.get(codename='change_servicediscountservice'),
        Permission.objects.get(codename='view_servicediscountservice'),
        Permission.objects.get(codename='delete_servicediscountservice'),
        Permission.objects.get(codename='add_invoiceservice'),
        Permission.objects.get(codename='change_invoiceservice'),
        Permission.objects.get(codename='view_invoiceservice'),
        Permission.objects.get(codename='delete_invoiceservice'),
        Permission.objects.get(codename='add_city'),
        Permission.objects.get(codename='change_city'),
        Permission.objects.get(codename='view_city'),
        Permission.objects.get(codename='delete_city'),
        Permission.objects.get(codename='add_customer'),
        Permission.objects.get(codename='change_customer'),
        Permission.objects.get(codename='view_customer'),
        Permission.objects.get(codename='delete_customer'),
        Permission.objects.get(codename='add_postalcode'),
        Permission.objects.get(codename='change_postalcode'),
        Permission.objects.get(codename='view_postalcode'),
        Permission.objects.get(codename='delete_postalcode'),
        Permission.objects.get(codename='add_address'),
        Permission.objects.get(codename='change_address'),
        Permission.objects.get(codename='view_address'),
        Permission.objects.get(codename='delete_address'),
        Permission.objects.get(codename='add_package'),
        Permission.objects.get(codename='change_package'),
        Permission.objects.get(codename='view_package'),
        Permission.objects.get(codename='delete_package'),
        Permission.objects.get(codename='add_packagediscount'),
        Permission.objects.get(codename='change_packagediscount'),
        Permission.objects.get(codename='view_packagediscount'),
        Permission.objects.get(codename='delete_packagediscount'),
        Permission.objects.get(codename='add_packagediscountpackage'),
        Permission.objects.get(codename='change_packagediscountpackage'),
        Permission.objects.get(codename='view_packagediscountpackage'),
        Permission.objects.get(codename='delete_packagediscountpackage'),
        Permission.objects.get(codename='add_invoicepackage'),
        Permission.objects.get(codename='change_invoicepackage'),
        Permission.objects.get(codename='view_invoicepackage'),
        Permission.objects.get(codename='delete_invoicepackage')
    ]

    for p in permissions:
        administrator_group.permissions.add(p)

    return administrator_group
