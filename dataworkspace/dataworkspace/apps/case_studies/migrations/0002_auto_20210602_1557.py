# Generated by Django 3.0.14 on 2021-06-02 15:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("case_studies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="casestudy",
            name="quote_text",
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
