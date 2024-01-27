# Generated by Django 5.0.1 on 2024-01-27 08:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone",
                    models.CharField(
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{10}$", message="Phone number must be 10 digits"
                            )
                        ],
                    ),
                ),
                ("date", models.DateField()),
                ("time", models.CharField(blank=True, max_length=255)),
                ("guests", models.PositiveIntegerField()),
                ("message", models.TextField(blank=True)),
            ],
        ),
    ]