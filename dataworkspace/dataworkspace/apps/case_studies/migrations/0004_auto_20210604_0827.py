# Generated by Django 3.0.14 on 2021-06-04 08:27

from django.db import migrations, models
import dataworkspace.apps.core.storage


class Migration(migrations.Migration):

    dependencies = [
        ('case_studies', '0003_auto_20210603_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudy',
            name='image',
            field=models.FileField(
                blank=True,
                storage=dataworkspace.apps.core.storage.S3FileStorage(
                    location='case-studies'
                ),
                upload_to='',
            ),
        ),
    ]