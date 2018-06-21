from django.db import models

# Create your models here.
class customer(models.Model):
    user_firstname  = models.CharField(max_length=128)
    user_lastname = models.CharField(max_length=128)
    user_email = models.EmailField()