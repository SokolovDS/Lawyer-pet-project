# Generated by Django 3.0 on 2019-12-13 20:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_auto_20191213_2319'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Subscriber',
        ),
    ]