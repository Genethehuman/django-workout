# Generated by Django 4.0.6 on 2022-07-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_sender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailsender',
            name='to_emails',
            field=models.CharField(max_length=500, null=True),
        ),
    ]