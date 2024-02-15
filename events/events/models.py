from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

class Events(models.Model):
    STATUS_CHOICES = (
        ('принято','Принято' ),
        ('отклонено', 'Отклонено'),
        ('в рассмотрении', 'В рассмотрении')

    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    id_user = models.ForeignKey(User, related_name='event', on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=100)
    id_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='в рассмотрении')

class Meta:
    ordering = ('-date',)

def __str__(self):
    return self.name


#id*|name*|id_user|date*|place*|description*|id_status*
#Status: id_status|name(принято/отклонено/в рассмотрении)