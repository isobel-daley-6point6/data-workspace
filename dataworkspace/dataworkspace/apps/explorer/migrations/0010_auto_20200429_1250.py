# Generated by Django 3.0.5 on 2020-04-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("explorer", "0009_fieldschema_modelschema"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fieldschema",
            name="name",
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name="modelschema",
            name="name",
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
