# Generated by Django 4.0.6 on 2022-07-26 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_sender', '0010_alter_mailsender_uniq_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailsender',
            name='uniq_id',
            field=models.CharField(default='64fad904', max_length=120),
        ),
    ]
