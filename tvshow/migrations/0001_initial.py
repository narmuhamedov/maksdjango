# Generated by Django 4.1 on 2022-10-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
                ('genre', models.CharField(choices=[('HORROR', 'HORROR'), ('COMEDY', 'COMEDY'), ('MELODRAMME', 'MELODRAMME'), ('HISTORY', 'HISTORY'), ('ADVENTURE', 'ADVENTURE'), ('ANIME', 'ANIME')], max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
        ),
    ]