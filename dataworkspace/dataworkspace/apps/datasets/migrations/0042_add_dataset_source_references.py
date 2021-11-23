# Generated by Django 3.0.5 on 2020-04-15 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("datasets", "0041_auto_20200416_1939")]

    operations = [
        migrations.CreateModel(
            name="DatasetReferenceCode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                (
                    "code",
                    models.CharField(
                        help_text="Short code to identify the source (eg. DH for Data Hub, EW for Export Wins)",
                        max_length=20,
                        unique=True,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("counter", models.IntegerField(default=0)),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="customdatasetquery",
            name="reference_number",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="sourcelink",
            name="reference_number",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="sourcetable",
            name="reference_number",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="sourceview",
            name="reference_number",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="dataset",
            name="reference_code",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="datasets.DatasetReferenceCode",
            ),
        ),
    ]
