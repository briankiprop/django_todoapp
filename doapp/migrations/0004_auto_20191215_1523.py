# Generated by Django 2.2.7 on 2019-12-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doapp', '0003_auto_20191215_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='head',
            field=models.CharField(default='headline for to do', max_length=100),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo',
            field=models.TextField(default='brief on what to do'),
        ),
    ]