from django.db import models

# Create your models here.





class Students(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="inactive")



class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE, null=True)
