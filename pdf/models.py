from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    summary=models.TextField(max_length=2000)
    degree=models.CharField(max_length=200)
    school=models.CharField(max_length=200)
    university=models.CharField(max_length=500) 
    previous_Work=models.TextField(max_length=2000) 
    skills=models.TextField(max_length=2000)