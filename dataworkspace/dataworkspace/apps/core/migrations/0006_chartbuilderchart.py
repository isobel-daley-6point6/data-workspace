# Generated by Django 3.2.12 on 2022-04-01 15:19

import uuid

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

import dataworkspace.apps.core.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("explorer", "0018_chartbuilderchart_thumbnail"),
        ("core", "0005_alter_usersatisfactionsurvey_how_satisfied"),
    ]

    operations = [
        # migrations.RunSQL("TRUNCATE TABLE datasets_datasetchartbuilderchart"),
        migrations.CreateModel(
            name="ChartBuilderChart",
            fields=[
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("chart_config", models.JSONField(null=True)),
                (
                    "thumbnail",
                    models.FileField(
                        blank=True,
                        null=True,
                        storage=dataworkspace.apps.core.storage.S3FileStorage(
                            location="chart-builder-thumbnails"
                        ),
                        upload_to="",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="created+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "query_log",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="chart",
                        to="explorer.querylog",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="updated+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-created_date",),
            },
        ),
    ]