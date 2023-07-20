# Generated by Django 3.2.8 on 2022-02-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploaded_images/', verbose_name='image')),
            ],
        ),
    ]
