# Generated by Django 3.0.5 on 2020-04-24 08:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datasets", "0045_auto_20200421_0904")]

    operations = [
        migrations.AddField(
            model_name="visualisationcatalogueitem",
            name="eligibility_criteria",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=256), null=True, size=None
            ),
        )
    ]
