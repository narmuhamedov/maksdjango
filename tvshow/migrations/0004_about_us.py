# Generated by Django 4.1 on 2022-10-25 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshow', '0003_alter_tvshow_trailers_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('work_year', models.IntegerField(max_length=20)),
            ],
        ),
    ]