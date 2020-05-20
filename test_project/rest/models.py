import uuid
from django.db import models

# Create your models here.
class Post(models.Model):
    sender = models.CharField(
        max_length=20,
        blank=False,
        verbose_name='sender name'
    )
    message = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='message'
    )