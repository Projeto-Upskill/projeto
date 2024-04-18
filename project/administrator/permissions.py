from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Administrator


def create_permissions(codename, name, content_type):
    new_permission = Permission.objects.create(
        codename=codename,
        name=name,
        content_type=content_type
    )
    return new_permission


# menu_operators_permission = create_permissions(
#     codename='view_menu_operators',
#     name='can view menu operators',
#     content_type=ContentType.objects.get_for_model(Administrator)
# )
#
# menu_customers_permission = create_permissions(
#     codename='view_menu_customers',
#     name='can view menu customers',
#     content_type=ContentType.objects.get_for_model(Administrator)
# )
#
# menu_packages_permission = create_permissions(
#     codename='view_menu_packages',
#     name='can view menu packages',
#     content_type=ContentType.objects.get_for_model(Administrator)
# )
#
# menu_discounts_permission = create_permissions(
#     codename='view_menu_discounts',
#     name='can view menu discounts',
#     content_type=ContentType.objects.get_for_model(Administrator)
# )
#
# menu_services_permission = create_permissions(
#     codename='view_menu_services',
#     name='can view menu services',
#     content_type=ContentType.objects.get_for_model(Administrator)
# )


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
        Permission.objects.get(codename='delete_invoicepackage'),
        Permission.objects.get(codename='view_administrator_index'),
        Permission.objects.get(codename='view_menu_operators'),
        Permission.objects.get(codename='view_menu_customers'),
        Permission.objects.get(codename='view_menu_packages'),
        Permission.objects.get(codename='view_menu_discounts'),
        Permission.objects.get(codename='view_menu_services')
    ]

    for p in permissions:
        administrator_group.permissions.add(p)

    return administrator_group
