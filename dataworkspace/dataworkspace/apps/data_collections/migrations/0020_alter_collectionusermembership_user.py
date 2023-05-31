# Generated by Django 3.2.19 on 2023-05-11 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0013_auto_20230511_1615"),
        ("data_collections", "0019_alter_collectionusermembership_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collectionusermembership",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="collection_memberships",
                to="core.dataworkspaceuser",
            ),
        ),
    ]