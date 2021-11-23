# Generated by Django 3.0.12 on 2021-05-10 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventlog", "0007_remove_google_data_studio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventlog",
            name="event_type",
            field=models.IntegerField(
                choices=[
                    (1, "Dataset source link download"),
                    (2, "Dataset source table download"),
                    (3, "Reference dataset download"),
                    (4, "Table data download"),
                    (5, "SQL query download"),
                    (6, "Dataset source view download"),
                    (7, "Visualisation approved"),
                    (8, "Visualisation unapproved"),
                    (9, "Dataset access request"),
                    (10, "Granted dataset permission"),
                    (11, "Revoked dataset permission"),
                    (12, "Granted user permission"),
                    (13, "Revoked user permission"),
                    (14, "Granted visualisation permission"),
                    (15, "Revoked visualisation permission"),
                    (16, "Set dataset user access type"),
                    (17, "View AWS QuickSight visualisation"),
                    (19, "Saved a query in Data Explorer"),
                    (20, "View Superset visualisation"),
                ]
            ),
        ),
    ]
