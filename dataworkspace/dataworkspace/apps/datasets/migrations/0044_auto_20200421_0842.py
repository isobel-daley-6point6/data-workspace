# Generated by Django 3.0.5 on 2020-04-21 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("datasets", "0043_merge_20200420_1541")]

    operations = [
        migrations.AlterModelOptions(name="datasetreferencecode", options={"ordering": ("code")})
    ]
