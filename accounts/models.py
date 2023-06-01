from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    photo = models.ImageField(upload_to='profile_images')

    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
