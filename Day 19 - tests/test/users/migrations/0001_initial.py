# Generated by Django 4.0 on 2022-03-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('user_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=256)),
                ('address', models.CharField(max_length=70)),
                ('remmeber_me', models.BooleanField()),
            ],
        ),
    ]
