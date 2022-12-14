# Generated by Django 4.0.6 on 2022-07-26 05:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailSender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(default=uuid.uuid4, max_length=120, null=True)),
                ('to_emails', models.CharField(max_length=500, null=True)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('email_file', models.FileField(blank=True, null=True, upload_to='uploads')),
            ],
        ),
    ]
