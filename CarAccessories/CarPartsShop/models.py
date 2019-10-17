from django.db import models
class RegisterUser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32)
class UserInfo(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=32)
# Create your models here.
