# Generated by Django 5.1.7 on 2025-03-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_important',
            field=models.BooleanField(default=False),
        ),
    ]
