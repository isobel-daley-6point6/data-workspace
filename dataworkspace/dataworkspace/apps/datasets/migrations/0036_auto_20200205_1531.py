# Generated by Django 2.2.10 on 2020-02-05 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("datasets", "0035_migrate_group_asset_manager_data")]

    operations = [
        migrations.AlterField(
            model_name="dataset",
            name="grouping",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="datasets.DataGrouping",
            ),
        ),
        migrations.AlterField(
            model_name="referencedataset",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="datasets.DataGrouping",
            ),
        ),
    ]
