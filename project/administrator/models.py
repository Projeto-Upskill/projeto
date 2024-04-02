import string
import random
from django.db import models
from django.contrib.auth.models import User
import smtplib
from email.mime.text import MIMEText


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user')
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
            self.user.set_password(self.generate_password)
            self.user.save()
        else:
            # Existing user
            self.user.first_name = self.first_name
            self.user.last_name = self.last_name
            self.user.email = self.email
            self.user.save(update_fields=['first_name', 'last_name', 'email'])

        super().save(*args, **kwargs)

    @property
    def generate_password(self):
        # Generate a random password with uppercase and lowercase letters, numbers, and special characters
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for i in range(12))

    def send_welcome_email(self, user):
        from_email = "projetoupskill@gmail.com"
        password = "Upskill@20232024"

        msg = MIMEText(f"Dear {user.first_name},\n\nWelcome to our website!\n\nYour username is {user.username}\nYour password is {user.password}\n\nThank you for registering.")
        msg["Subject"] = "Welcome to Our Website!"
        msg["From"] = "projetoupskill@gmail.com"
        msg["To"] = user.email

        try:
            server = smtplib.SMTP("smtp.example.com", 587)
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, [user.email], msg.as_string())
            server.quit()
        except Exception as e:
            print(f"Error sending email: {e}")

    @property
    def generate_username(self):
        return f"{self.last_name}.{self.first_name}"
