import string
import random
from django.db import models
from django.contrib.auth.models import User
from django.core import mail


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

    # @property
    # def generate_password(self):
    #     # Generate a random password with uppercase and lowercase letters, numbers, and special characters
    #     characters = string.ascii_letters + string.digits + string.punctuation
    #     return ''.join(random.choice(characters) for i in range(12))

    # def send_welcome_email(self, user):
    #     try:
    #         if not user.has_usable_password():
    #             user.set_unusable_password()
    #             user.password = self.generate_password
    #             user.save()
    #         subject = 'Welcome to Our Website!'
    #         message = f"Dear {user.first_name},\n\nWelcome to our website!\n\nYour username is {user.username}\nYour password is {user.password}\n\nThank you for registering."
    #         email_from = EMAIL_HOST_USER
    #         recipient_list = [f'{user.email}', ]
    #
    #         connection = mail.get_connection(username=EMAIL_HOST_USER,
    #                                          password=EMAIL_HOST_PASSWORD,
    #                                          host=EMAIL_HOST,
    #                                          port=EMAIL_PORT,
    #                                          use_tls=EMAIL_USE_TLS)
    #
    #         mail.send_mail(subject, message, email_from, recipient_list, connection=connection, fail_silently=False)
    #         print(f"{user.email} {user.first_name}")
    #         connection.close()
    #     except Exception as e:
    #         print(f"Error sending email: {e}")

    # @property
    # def generate_username(self):
    #     return f"{self.last_name}.{self.first_name}"
