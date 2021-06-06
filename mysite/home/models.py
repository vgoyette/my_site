from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	img = models.ImageField(upload_to='static/img/')

class Contact(models.Model):
	email = models.EmailField()
	subject = models.CharField(max_length=255)
	message = models.TextField()

	def __str__(self):
		return self.email
