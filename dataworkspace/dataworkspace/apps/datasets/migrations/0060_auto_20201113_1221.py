# Generated by Django 3.0.8 on 2020-11-13 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0059_migrate_source_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dataset",
            name="source_tags",
        ),
        migrations.RemoveField(
            model_name="referencedataset",
            name="source_tags",
        ),
        migrations.DeleteModel(
            name="SourceTag",
        ),
    ]
