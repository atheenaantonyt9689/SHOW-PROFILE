from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Registration(models.Model):
    userid = models.EmailField(max_length=35, primary_key=True)
    password=models.CharField(max_length=20)

class Login(models.Model):
    userid = models.EmailField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
