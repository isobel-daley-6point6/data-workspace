# Generated by Django 3.0.5 on 2020-04-21 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("eventlog", "0003_auto_20191009_1107")]

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
                ]
            ),
        )
    ]
