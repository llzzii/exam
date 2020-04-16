# Generated by Django 2.2 on 2020-04-13 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('keys', models.CharField(max_length=255)),
                ('a_key', models.CharField(max_length=255)),
                ('b_key', models.CharField(max_length=255)),
                ('c_key', models.CharField(max_length=255)),
                ('d_key', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('resolve', models.CharField(max_length=255)),
            ],
        ),
    ]