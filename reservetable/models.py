import email
from django.db import models

# Create your models here.
class usermessage(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True)
    email=models.CharField(max_length=200,blank=True, null=True)
    number=models.CharField(max_length=200,blank=True, null=True)
    message=models.TextField(max_length=500,blank=True, null=True)
    
