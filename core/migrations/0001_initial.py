# Generated by Django 5.0.4 on 2024-04-04 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Widget",
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
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("quantity", models.IntegerField()),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
