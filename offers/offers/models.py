from django.db import models

from django.contrib.auth.models import User


class Offer(models.Model):
    STATUS_CHOICES = (
        ('принята', 'Принята'),
        ('отклонена', 'Отклонена'),
        ('отправлена', 'Отправлена')

    )
    id = models.AutoField(primary_key=True)
    id_from = models.IntegerField()
    id_to = models.IntegerField()
    id_book = models.IntegerField()
    id_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Отправлена')


class Meta:
    ordering = ('-date',)


def __str__(self):
    return self.name