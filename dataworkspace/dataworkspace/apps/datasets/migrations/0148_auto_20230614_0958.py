# Generated by Django 3.2.18 on 2023-06-14 09:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("datasets", "0147_sourcetable_disable_data_grid_interaction"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataset",
            name="data_catalogue_editors",
            field=models.ManyToManyField(
                blank=True,
                related_name="data_catalogue_edit_datasets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="visualisationcatalogueitem",
            name="data_catalogue_editors",
            field=models.ManyToManyField(
                blank=True,
                related_name="data_catalogue_edit_visualisations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]