# Generated by Django 4.2.5 on 2023-09-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0002_appuser_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="appuser",
            name="area",
            field=models.TextField(default="Select", max_length=100),
            preserve_default=False,
        ),
    ]
