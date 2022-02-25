# Generated by Django 3.2.12 on 2022-02-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0019_alter_applicationtemplate_group_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicationtemplate",
            name="group_name",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Visualisation Tools", "Visualisation Tools"),
                    ("Data Analysis Tools", "Data Analysis Tools"),
                    ("Data Management Tools", "Data Management Tools"),
                    (
                        "Integrated Development Environments",
                        "Integrated Development Environments",
                    ),
                ],
                default="Data Analysis Tools",
                max_length=50,
                null=True,
            ),
        ),
    ]
