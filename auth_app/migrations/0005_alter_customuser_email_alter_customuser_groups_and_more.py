# Generated by Django 5.0.7 on 2024-11-04 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        (
            "auth_app",
            "0004_alter_customuser_email_alter_customuser_groups_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="groups",
            field=models.ManyToManyField(
                blank=True, related_name="customuser_set", to="auth.group"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True, related_name="customuser_set", to="auth.permission"
            ),
        ),
    ]
