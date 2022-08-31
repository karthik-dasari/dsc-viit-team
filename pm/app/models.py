from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Passmanager(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    site=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

