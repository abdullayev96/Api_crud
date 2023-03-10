# Generated by Django 4.1.7 on 2023-02-14 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='images')),
                ('price', models.IntegerField()),
                ('number', models.CharField(max_length=200)),
                ('place', models.IntegerField(choices=[(1, 'Uzbekistan'), (2, 'Rossiya'), (3, 'Tukiya'), (4, 'Saudiya'), (5, 'Xitoy'), (6, 'Germaniya'), (7, 'Usa'), (8, 'Japon')], default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.customer')),
            ],
        ),
    ]
