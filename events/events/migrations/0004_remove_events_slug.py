# Generated by Django 5.0.2 on 2024-02-15 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_events_id_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='slug',
        ),
    ]
