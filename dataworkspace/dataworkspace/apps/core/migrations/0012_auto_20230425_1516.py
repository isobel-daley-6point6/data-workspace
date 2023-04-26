# Generated by Django 3.2.18 on 2023-04-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_auto_20221017_1448"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="databaseuser",
            options={"ordering": ("created_date",)},
        ),
        migrations.AlterField(
            model_name="databaseuser",
            name="username",
            field=models.CharField(db_index=True, max_length=256),
        ),
    ]
