# Generated by Django 4.0.6 on 2022-07-26 04:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mail_sender', '0011_alter_mailsender_uniq_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailsender',
            name='uniq_id',
        ),
        migrations.AddField(
            model_name='mailsender',
            name='unique_id',
            field=models.CharField(default=uuid.uuid4, max_length=8),
        ),
    ]
