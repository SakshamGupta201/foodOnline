# Generated by Django 5.1.2 on 2024-10-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("username", models.CharField(max_length=50, unique=True)),
                ("email", models.EmailField(max_length=50, unique=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "role",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Restaurant"), (2, "Customer")], default=2
                    ),
                ),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("last_login", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]