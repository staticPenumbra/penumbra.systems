from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=63)
	slug = models.SlugField()
	text = models.TextField()
	pub_date = models.DateField()
	
class Media(models.Model):
	title = models.CharField(max_length=63)
	type = models.CharField(max_length=10)
	slug = models.SlugField()
	link = models.URLField()
	pub_date = models.DateField()