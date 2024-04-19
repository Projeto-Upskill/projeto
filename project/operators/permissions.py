from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_operators_group(**kwargs):
    operator_group, created = Group.objects.get_or_create(name='operator_group')
    permissions = [
        # O Operador pode atribuir e remover um pacote comercial a um cliente
        # this is invoiceservices and invoice packages
        Permission.objects.get(codename='add_invoicepackage'), #ok
        Permission.objects.get(codename='add_invoiceservice'), #ok
        Permission.objects.get(codename='delete_invoicepackage'), #ok
        Permission.objects.get(codename='delete_invoiceservice'), #ok

        #O Operador pode visualizar a lista de pacotes comerciais disponíveis.
        Permission.objects.get(codename='view_package'), #ok
        Permission.objects.get(codename='view_service'), #ok

        # O Operador pode atribuir e remover uma promoção a um pacote comercial
        Permission.objects.get(codename='add_packagediscount'), #ok
        Permission.objects.get(codename='delete_packagediscount'), #ok
        Permission.objects.get(codename='add_servicediscount'), #ok
        Permission.objects.get(codename='delete_servicediscount'), #ok

        #O Operador pode visualizar todas as promoções de um cliente.
       # Permission.objects.get(codename='view_clientpromotion'), #nope

        # O Operador pode visualizar a lista de promoções disponíveis.
        Permission.objects.get(codename='view_packagediscount'), #ok
        Permission.objects.get(codename='view_servicediscount'),  # ok
    ]

    # this next line is to delete all permissions if some are added that we dont want
    #operator_group.permissions.clear()
    for p in permissions:
        operator_group.permissions.add(p)

    return operator_group
