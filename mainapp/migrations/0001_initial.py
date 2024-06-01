# Generated by Django 4.2.10 on 2024-05-31 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SavedData",
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
                ("username", models.CharField(max_length=255)),
                ("abstract", models.CharField(max_length=10000000)),
                ("keywords", models.CharField(max_length=100000)),
            ],
        ),
    ]