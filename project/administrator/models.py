from django.db import models
from django.contrib.auth.models import User


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user', related_name='administrators')
    id_administrator = models.AutoField(primary_key=True, verbose_name='id administrator')
    first_name = models.CharField(max_length=500, verbose_name='first name')
    last_name = models.CharField(max_length=500, verbose_name='last name')
    email = models.EmailField(max_length=300, verbose_name='email')
    birth_date = models.DateField(verbose_name='birth date')
    active = models.BooleanField(default=True, verbose_name='active')

    class Meta:
        db_table = 'administrator'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_administrator} {self.first_name} {self.last_name} {self.email} {self.birth_date} {self.active}"

    def save(self, *args, **kwargs):
        if not self.user.id:
            self.user.set_password(self.user.password)
            self.user.save()
        else:
            # Existing user
            self.user.first_name = self.first_name
            self.user.last_name = self.last_name
            self.user.email = self.email
            self.user.save(update_fields=['first_name', 'last_name', 'email'])

        super().save(*args, **kwargs)
