# Generated by Django 2.0.5 on 2018-05-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_auto_20180510_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='tests.Answer'),
        ),
    ]
