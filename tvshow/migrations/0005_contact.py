# Generated by Django 4.1 on 2022-11-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshow', '0004_about_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('work_years', models.DateField()),
            ],
        ),
    ]