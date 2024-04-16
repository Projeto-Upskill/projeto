from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_operators_group(**kwargs):
    operator_group, created = Group.objects.get_or_create(name='operator_group')
    permissions = [
        Permission.objects.get(codename='change_service'),
        Permission.objects.get(codename='view_service'),
        Permission.objects.get(codename='view_servicediscount'),
        Permission.objects.get(codename='view_servicetype'),
        Permission.objects.get(codename='add_servicediscountservice'),
        Permission.objects.get(codename='change_servicediscountservice'),
        Permission.objects.get(codename='view_servicediscountservice'),
        Permission.objects.get(codename='delete_servicediscountservice'),
        Permission.objects.get(codename='add_invoiceservice'),
        Permission.objects.get(codename='view_invoiceservice'),
        Permission.objects.get(codename='view_customer'),
        Permission.objects.get(codename='view_address'),
        Permission.objects.get(codename='view_package'),
        Permission.objects.get(codename='view_packagediscount'),
        Permission.objects.get(codename='add_packagediscountpackage'),
        Permission.objects.get(codename='change_packagediscountpackage'),
        Permission.objects.get(codename='view_packagediscountpackage'),
        Permission.objects.get(codename='delete_packagediscountpackage'),
        Permission.objects.get(codename='add_invoicepackage'),
        Permission.objects.get(codename='view_invoicepackage')
    ]

    for p in permissions:
        operator_group.permissions.add(p)

    return operator_group
