# Generated by Django 3.0.4 on 2020-03-22 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblogger', '0007_auto_20200322_1118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id', 'created_at', 'updated_at', 'title'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
