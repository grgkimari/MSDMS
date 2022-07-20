from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(blank=False, null = False, verbose_name="email",unique=True)
    user_type = models.CharField(blank = False, null = False, verbose_name = "usertype", max_length=25)
    date_joined = models.DateField(auto_now_add=True)

    USERNAME_FIELD: 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email
