# Generated by Django 4.1.4 on 2023-03-23 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
