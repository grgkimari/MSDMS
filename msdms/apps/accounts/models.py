from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    accountType = models.CharField(verbose_name="accountType", blank = False, null=True)