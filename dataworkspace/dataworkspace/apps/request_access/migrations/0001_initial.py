# Generated by Django 3.2.4 on 2021-08-12 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import dataworkspace.apps.core.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AccessRequest",
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
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                ("catalogue_item_id", models.UUIDField(null=True)),
                ("contact_email", models.CharField(max_length=256, null=True)),
                ("reason_for_access", models.TextField(null=True)),
                (
                    "training_screenshot",
                    models.FileField(
                        blank=True,
                        null=True,
                        storage=dataworkspace.apps.core.storage.S3FileStorage(
                            location="training_screenshots"
                        ),
                        upload_to="",
                    ),
                ),
                ("spss_and_stata", models.BooleanField(blank=True, default=False)),
                (
                    "line_manager_email_address",
                    models.CharField(max_length=256, null=True),
                ),
                ("reason_for_spss_and_stata", models.TextField(null=True)),
                (
                    "zendesk_reference_number",
                    models.CharField(max_length=256, null=True),
                ),
                (
                    "requester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="access_requests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
    ]
