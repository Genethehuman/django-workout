# Generated by Django 4.0.6 on 2022-07-26 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_sender', '0017_alter_mailsender_uniq_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailsender',
            name='uniq_id',
        ),
    ]
