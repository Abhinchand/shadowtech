from django.contrib.auth.models import AbstractUser
from django.db.models import *

# Create your models here.


class Shadow_user(AbstractUser):
    image = ImageField(upload_to='images')