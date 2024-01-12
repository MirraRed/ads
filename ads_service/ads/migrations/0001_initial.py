# Generated by Django 4.2.7 on 2024-01-12 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=25, unique=True)),
                ('user_password', models.CharField(max_length=25)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.location')),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('ad_text', models.CharField(max_length=700)),
                ('is_public', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.user')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.location')),
            ],
        ),
    ]
