# Generated by Django 4.0.3 on 2022-03-21 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='overview',
        ),
    ]
