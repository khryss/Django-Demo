# Generated by Django 2.0.5 on 2018-05-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20180510_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='tests',
            field=models.ManyToManyField(to='tests.Test'),
        ),
    ]
