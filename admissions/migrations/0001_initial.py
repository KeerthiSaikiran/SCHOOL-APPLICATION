# Generated by Django 4.2.3 on 2023-08-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fathername', models.CharField(max_length=255)),
                ('classname', models.IntegerField()),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
    ]