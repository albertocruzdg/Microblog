from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(User)
	text = models.TextField()
	date = models.DateTimeField()
	def __unicode__(self):
		return self.user.get_full_name() + ': ' + self.text

class Comment(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	date = models.DateTimeField()
	text = models.TextField()

	def __unicode__(self):
		return text