# Generated by Django 5.0.7 on 2024-11-04 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
