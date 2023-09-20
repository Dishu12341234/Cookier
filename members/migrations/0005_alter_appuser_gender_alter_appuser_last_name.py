# Generated by Django 4.2.5 on 2023-09-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0004_alter_appuser_area"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appuser",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                default="M",
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="appuser",
            name="last_name",
            field=models.CharField(default="", max_length=30),
        ),
    ]
