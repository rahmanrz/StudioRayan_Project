# Generated by Django 5.0.3 on 2024-03-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='projects')),
            ],
        ),
    ]
