# Generated by Django 3.2.5 on 2021-09-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("explorer", "0015_auto_20210104_0923"),
    ]

    operations = [
        migrations.AddField(
            model_name="querylog",
            name="page_size",
            field=models.IntegerField(default=1000, null=True),
        ),
    ]
