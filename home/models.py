from django.db import models
from requests import request
from sqlalchemy import null




class task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

	def __str__(self):
		return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    date = models.DateField()

class Queries(models.Model):
    name = models.CharField(max_length=50)
    Ename = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
