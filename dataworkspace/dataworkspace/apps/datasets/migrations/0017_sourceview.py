# Generated by Django 2.2.3 on 2019-10-09 14:44

import uuid
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("core", "0001_initial"), ("datasets", "0016_auto_20191009_1341")]

    operations = [
        migrations.CreateModel(
            name="SourceView",
            fields=[
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Used as the displayed text in the download link",
                        max_length=1024,
                    ),
                ),
                (
                    "schema",
                    models.CharField(
                        default="public",
                        max_length=1024,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^[a-zA-Z][a-zA-Z0-9_\\.]*$"
                            )
                        ],
                    ),
                ),
                (
                    "view",
                    models.CharField(
                        max_length=1024,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^[a-zA-Z][a-zA-Z0-9_\\.]*$"
                            )
                        ],
                    ),
                ),
                (
                    "database",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.Database",
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datasets.DataSet",
                    ),
                ),
            ],
            options={"abstract": False},
        )
    ]
