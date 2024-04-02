from django.db import models

class operators(models.Model):
	id_operator = models.AutoField(primary_key=True, verbose_name='id_operator')
	name = models.CharField(max_length=500)
	email = models.EmailField(max_length=300)
	birth_date = models.DateField()
	active = models.BooleanField()

	class Meta:
		db_table = 'operators'

	
