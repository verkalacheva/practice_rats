from django.db import models
from django.contrib.auth.models import User


class RoleField(models.CharField):
    ROLE_CHOICES = [
        ('bookcrosser', 'bookcrosser'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    ]

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = self.ROLE_CHOICES
        kwargs['max_length'] = 11
        kwargs['blank'] = False
        kwargs['null'] = False
        super().__init__(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    role = RoleField(default='bookcrosser')

    def __str__(self):
        return self.user.username
    
