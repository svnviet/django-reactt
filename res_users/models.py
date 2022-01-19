from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.full_name
