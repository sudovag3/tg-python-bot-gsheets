# Generated by Django 3.1.1 on 2020-09-29 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='onWhatQuestion',
        ),
    ]