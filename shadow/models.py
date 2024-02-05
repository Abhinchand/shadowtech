from django.contrib.auth.models import AbstractUser
from django.db.models import *
from django.db import models

# Create your models here.


class Shadow_user(AbstractUser):
    image = ImageField(upload_to='images')

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.IntegerField()
    subject = models.CharField(max_length=250)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ["-timestamp", "-update"]



