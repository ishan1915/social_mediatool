# Generated by Django 5.0.6 on 2024-07-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_task_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='admin_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
