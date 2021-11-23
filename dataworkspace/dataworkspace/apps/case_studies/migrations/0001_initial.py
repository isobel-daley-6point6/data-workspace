# Generated by Django 3.0.14 on 2021-05-28 14:15

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CaseStudy",
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
                ("slug", models.SlugField()),
                ("published", models.BooleanField(default=False)),
                ("publish_date", models.DateTimeField(null=True)),
                ("name", models.CharField(max_length=255)),
                ("short_description", models.CharField(max_length=255)),
                ("department_name", models.CharField(blank=True, max_length=255)),
                ("service_name", models.CharField(blank=True, max_length=255)),
                ("outcome", models.CharField(blank=True, max_length=255)),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("background", ckeditor.fields.RichTextField(blank=True)),
                ("solution", ckeditor.fields.RichTextField(blank=True)),
                ("impact", ckeditor.fields.RichTextField(blank=True)),
                ("quote_title", models.CharField(blank=True, max_length=255)),
                ("quote_text", models.CharField(blank=True, max_length=255)),
                ("quote_full_name", models.CharField(blank=True, max_length=255)),
                ("quote_department_name", models.CharField(blank=True, max_length=255)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="created+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="updated+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Case studies",
                "ordering": ("-created_date",),
            },
        ),
    ]
