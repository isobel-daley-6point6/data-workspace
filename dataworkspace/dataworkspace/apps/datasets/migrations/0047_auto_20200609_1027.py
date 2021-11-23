# Generated by Django 3.0.5 on 2020-06-09 10:27

from django.conf import settings

from django.db import migrations, models
import django.db.models.deletion


def copy_permissions(apps, schema_editor):
    VisualisationCatalogueItem = apps.get_model("datasets", "VisualisationCatalogueItem")
    VisualisationUserPermission = apps.get_model("datasets", "VisualisationUserPermission")

    visualisations = VisualisationCatalogueItem.objects.all()
    for visualisation in visualisations:
        user_permissions = (
            visualisation.visualisation_template.applicationtemplateuserpermission_set.all()
        )

        for user_permission in user_permissions:
            VisualisationUserPermission.objects.create(
                visualisation=visualisation, user=user_permission.user
            )

        visualisation.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("datasets", "0046_visualisationcatalogueitem_eligibility_criteria"),
    ]

    operations = [
        migrations.AddField(
            model_name="visualisationcatalogueitem",
            name="user_access_type",
            field=models.CharField(
                choices=[
                    ("REQUIRES_AUTHENTICATION", "Requires authentication"),
                    ("REQUIRES_AUTHORIZATION", "Requires authorization"),
                ],
                default="REQUIRES_AUTHENTICATION",
                max_length=64,
            ),
        ),
        migrations.CreateModel(
            name="VisualisationUserPermission",
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
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "visualisation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datasets.VisualisationCatalogueItem",
                    ),
                ),
            ],
            options={
                "db_table": "app_visualisationuserpermission",
                "unique_together": {("user", "visualisation")},
            },
        ),
        migrations.RunPython(code=copy_permissions, reverse_code=noop),
    ]
