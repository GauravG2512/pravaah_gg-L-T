from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Middle Name")
    contact = models.CharField(max_length=15, blank=True, null=True, verbose_name="Contact Number")
    
    # Require email and make it unique
    email = models.EmailField(unique=True, verbose_name="Email Address")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        full_name = self.get_full_name()
        return full_name if full_name else self.username

    def get_full_name(self):
        names = [self.first_name, self.middle_name, self.last_name]
        return " ".join([name for name in names if name]).strip()
