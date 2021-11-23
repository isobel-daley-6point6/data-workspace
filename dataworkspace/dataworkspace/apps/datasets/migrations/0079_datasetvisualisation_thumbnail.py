# Generated by Django 3.0.14 on 2021-06-07 12:00

from django.db import migrations, models
import dataworkspace.apps.core.storage


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0078_auto_20210528_1642"),
    ]

    operations = [
        migrations.AddField(
            model_name="datasetvisualisation",
            name="thumbnail",
            field=models.FileField(
                blank=True,
                null=True,
                storage=dataworkspace.apps.core.storage.S3FileStorage(
                    location="visualisation-thumbnails"
                ),
                upload_to="",
            ),
        ),
    ]
