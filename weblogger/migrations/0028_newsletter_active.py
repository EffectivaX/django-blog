# Generated by Django 3.0.4 on 2020-04-14 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblogger', '0027_auto_20200415_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
