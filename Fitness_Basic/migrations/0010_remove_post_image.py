# Generated by Django 2.1.1 on 2018-09-15 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness_Basic', '0009_auto_20180914_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
