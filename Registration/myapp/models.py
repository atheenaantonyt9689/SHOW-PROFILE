from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Registration(models.Model):
    Name=models.CharField(max_length=20)
    Email= models.EmailField(max_length=35, primary_key=True)
    Password=models.CharField(max_length=20)


class Login(models.Model):
    Email = models.EmailField(max_length=20, primary_key=True)
    Password = models.CharField(max_length=20)
