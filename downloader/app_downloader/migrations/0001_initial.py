# Generated by Django 4.2.2 on 2023-06-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_name', models.CharField(max_length=255, verbose_name='Наименование объекта')),
                ('equipment_name', models.CharField(max_length=255, verbose_name='Наименование оборудования')),
                ('file', models.FileField(blank=True, upload_to='documents', verbose_name='Файл')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
