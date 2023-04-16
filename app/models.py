from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactModel(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=5)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.IntegerField()
    is_favourite = models.BooleanField(default=True)