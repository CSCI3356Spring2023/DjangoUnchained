# Generated by Django 4.1.5 on 2023-04-04 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('from_email', models.CharField(max_length=200)),
                ('to_email', models.CharField(max_length=200)),
            ],
        ),
    ]