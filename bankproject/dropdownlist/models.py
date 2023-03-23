from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class firstname(models.Model):
    name=models.CharField(max_length=250)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,blank=True,null=True)
    branch=models.ForeignKey(Branch,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.name
