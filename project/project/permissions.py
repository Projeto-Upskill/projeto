from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_superadmin_group(**kwargs):
    superadmin_group, created = Group.objects.get_or_create(name='superadmin_group')

    permissions = [
        Permission.objects.get(codename="add_administrator"),
        Permission.objects.get(codename="change_administrator"),
        Permission.objects.get(codename="delete_administrator"),
        Permission.objects.get(codename="view_administrator"),
    ]

    for p in permissions:
        superadmin_group.permissions.add(p)

    return superadmin_group
