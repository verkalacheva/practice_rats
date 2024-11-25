from django.db import models

class Offer(models.Model):
    STATUS_CHOICES = (
        ('предложена', 'Предложена'),
        ('скрыта', 'Скрыта'),
        ('отправлена', 'Отправлена'),
        ('принята', 'Принята'),
        ('отклонена', 'Отклонена'),
    )
    id = models.AutoField(primary_key=True)
    id_from = models.IntegerField()
    id_to = models.IntegerField()
    id_book = models.IntegerField()
    id_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Предложена')


class Meta:
    ordering = ('-date',)


def __str__(self):
    return self.name