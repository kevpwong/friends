from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Friendship(models.Model):
    user_friend = models.ForeignKey(User, related_name="userfriends")
    friend_friend = models.ForeignKey(User, related_name="friendfriends")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
