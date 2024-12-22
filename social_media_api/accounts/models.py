from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)

    def __str__(self):
        return self.username
