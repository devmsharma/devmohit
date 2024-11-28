# Generated by Django 4.0.1 on 2022-01-28 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('dob', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=255)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]