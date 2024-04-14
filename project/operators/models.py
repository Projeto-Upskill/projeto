from django.db import models
from django.contrib.auth.models import User


class Operators(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user', related_name='operators')
	id_operator = models.AutoField(primary_key=True, verbose_name='id_operator')
	first_name = models.CharField(max_length=500)
	last_name = models.CharField(max_length=500)
	email = models.EmailField(max_length=300)
	birth_date = models.DateField()
	admission_date = models.DateField()
	active = models.BooleanField()

	class Meta:
		db_table = 'Operators'

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
