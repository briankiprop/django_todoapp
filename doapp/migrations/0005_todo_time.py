# Generated by Django 2.2.7 on 2019-12-16 12:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doapp', '0004_auto_20191215_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Conversation Time'),
            preserve_default=False,
        ),
    ]