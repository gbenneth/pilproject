# Generated by Django 2.0.2 on 2018-04-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_firstname', models.CharField(max_length=128)),
                ('user_lastname', models.CharField(max_length=128)),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
