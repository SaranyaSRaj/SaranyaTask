from django.db import models

# Create your models here.
class Login(models.Model):
    name=models.CharField(max_length=250,unique=True)
    password=models.IntegerField()
    class meta:
        ordering=('name')
    def __str__(self):
        return self.name

class Register(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Registration(models.Model):
    name=models.CharField(max_length=250)