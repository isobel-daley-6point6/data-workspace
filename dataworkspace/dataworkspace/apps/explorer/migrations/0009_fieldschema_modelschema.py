# Generated by Django 3.0.5 on 2020-04-28 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("explorer", "0008_auto_20190308_1642"),
    ]

    operations = [
        migrations.CreateModel(
            name="FieldSchema",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=16)),
                (
                    "data_type",
                    models.CharField(
                        choices=[
                            ("character", "character"),
                            ("text", "text"),
                            ("integer", "integer"),
                            ("float", "float"),
                            ("boolean", "boolean"),
                            ("date", "date"),
                        ],
                        editable=False,
                        max_length=16,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="ModelSchema",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("_modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=32, unique=True)),
            ],
            options={"abstract": False},
        ),
    ]
