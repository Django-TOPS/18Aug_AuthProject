from django.db import models

# Create your models here.

class Signup(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField()

    def __str__(self):
        return self.fname