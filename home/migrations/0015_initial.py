# Generated by Django 4.1.7 on 2023-03-07 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0014_remove_seat_sro_delete_film_delete_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pic')),
                ('star', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('dimensional', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=100)),
                ('available', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('sro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film', to='home.film')),
            ],
        ),
    ]
