# Generated by Django 2.2 on 2020-04-16 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0005_auto_20200416_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='resolve',
            field=models.CharField(max_length=1000),
        ),
    ]
