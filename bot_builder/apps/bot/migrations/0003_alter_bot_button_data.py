# Generated by Django 5.1.1 on 2024-09-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_delete_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot_button',
            name='data',
            field=models.CharField(default='', max_length=255, verbose_name='Данные'),
        ),
    ]