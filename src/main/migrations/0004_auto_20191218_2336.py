# Generated by Django 3.0 on 2019-12-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_auto_20191213_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='patronymic',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='phone',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='surname',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
