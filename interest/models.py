from django.db import models

# Create your models here.
class Interest(models.Model):
	name = models.CharField(max_length=50)
	type = models.CharField(max_length=10, choices=(('social','Social'),('work','Work')))

	def __str__(self):
		return self.name