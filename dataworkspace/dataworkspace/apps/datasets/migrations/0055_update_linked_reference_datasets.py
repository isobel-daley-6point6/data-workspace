# Generated by Django 3.0.8 on 2020-09-21 16:13

from django.db import migrations, transaction


@transaction.atomic
def update_linked_reference_datasets(apps, schema_editor):
    ReferenceDatasetField = apps.get_model("datasets", "ReferenceDatasetField")
    for field in ReferenceDatasetField.objects.filter(data_type=8):
        linked_identifier_field = field.linked_reference_dataset.fields.get(is_identifier=True)
        linked_display_name_field = field.linked_reference_dataset.fields.get(is_display_name=True)

        # This will be used as the prefix in the new field name
        original_field_name = field.name
        # This will be used as the relationshp_name
        original_column_name = field.column_name

        # Modify existing linked reference dataset field to match
        # new structure and point it to the original identifier field
        field.name = f"{original_field_name}: {linked_identifier_field.name}"
        field.relationship_name = original_column_name
        field.column_name = None
        field.linked_reference_dataset_field = linked_identifier_field
        field.save()

        # Create new linked reference dataset field and point it to the
        # original display name field
        display_field = ReferenceDatasetField()
        display_field.reference_dataset = field.reference_dataset
        display_field.data_type = 8
        display_field.name = f"{original_field_name}: {linked_display_name_field.name}"
        display_field.description = linked_display_name_field.description
        display_field.relationship_name = original_column_name
        display_field.linked_reference_dataset_field = linked_display_name_field
        display_field.save()


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0054_auto_20200921_1610"),
    ]

    operations = [
        migrations.RunPython(update_linked_reference_datasets),
    ]
