# Generated by Django 3.2.8 on 2021-10-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='dt_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
