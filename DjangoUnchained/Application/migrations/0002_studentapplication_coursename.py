# Generated by Django 4.2 on 2023-05-03 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentapplication',
            name='courseName',
            field=models.CharField(default='N/A', max_length=100000),
            preserve_default=False,
        ),
    ]
