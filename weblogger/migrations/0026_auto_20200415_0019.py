# Generated by Django 3.0.4 on 2020-04-14 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblogger', '0025_auto_20200413_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='newsletter',
            old_name='email',
            new_name='your_email',
        ),
    ]
