# Generated by Django 3.2.16 on 2022-12-23 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_mo_deleteme'),
    ]

    operations = [
        migrations.AddField(
            model_name='mo_task',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
