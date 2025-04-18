# Generated by Django 4.2.16 on 2024-12-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="city",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="street",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="zip_code",
            field=models.CharField(default="", max_length=6),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="phone",
            field=models.CharField(default="", max_length=50),
        ),
    ]
