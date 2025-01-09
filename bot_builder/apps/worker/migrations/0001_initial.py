# Generated by Django 5.1.1 on 2024-09-26 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bot', '0002_delete_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ACCEPTED', 'Событие создано'), ('COMPLETED', 'Событие закончено')], max_length=110)),
                ('update_data', models.JSONField(default=dict, verbose_name='JSON объект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='bot.botuser')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
    ]
