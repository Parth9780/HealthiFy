# Generated by Django 5.0.6 on 2024-06-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UseName', models.CharField(max_length=150)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
    ]
