from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager


class Craig(models.Model):
    city = models.CharField(max_length=200)
    user = models.OneToOneField(User, null=True)

    class Meta:
        ordering = ['id']
# Create your models here.
