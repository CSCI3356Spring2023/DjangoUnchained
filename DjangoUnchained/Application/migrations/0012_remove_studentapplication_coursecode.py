# Generated by Django 4.1.7 on 2023-04-20 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Application", "0011_studentapplication_coursecode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentapplication",
            name="courseCode",
        ),
    ]
