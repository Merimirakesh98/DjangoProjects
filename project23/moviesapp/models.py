from django.db import models

class Movies(models.Model):
	name = models.CharField(max_length=50)
	hero = models.CharField( max_length=50)
	heroine = models.CharField(max_length=50)
	director = models.CharField(max_length=50)
	producer = models.CharField(max_length=50)
	music = models.CharField(max_length=50)
	release = models.CharField(max_length=50)
    
