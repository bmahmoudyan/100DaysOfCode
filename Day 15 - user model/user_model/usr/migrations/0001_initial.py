# Generated by Django 4.0 on 2022-03-17 19:31

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
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('username', models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='Email')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email Verified')),
                ('staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Admin')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
