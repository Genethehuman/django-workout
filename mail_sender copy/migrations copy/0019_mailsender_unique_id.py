# Generated by Django 4.0.6 on 2022-07-26 05:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mail_sender', '0018_remove_mailsender_uniq_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailsender',
            name='unique_id',
            field=models.CharField(default=uuid.uuid4, max_length=120, null=True),
        ),
    ]