# Generated by Django 4.2 on 2023-04-18 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0008_alter_courseadd_discussion_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseadd',
            name='days',
            field=models.CharField(choices=[('M/W/F', 'M/W/F'), ('T/Th', 'T/Th'), ('M/W', 'M/W'), ('M', 'M'), ('T', 'T'), ('W', 'W'), ('Th', 'Th'), ('F', 'F')], max_length=100, null=True),
        ),
    ]