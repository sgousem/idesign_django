from django.db import models

# Create your models here.
class Feature(models.Model):

    name = models.TextField()
    desc = models.TextField()
class form(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField('%d/%m/%Y')
    city = models.CharField(max_length=100)