# Generated by Django 3.2.20 on 2023-12-11 12:38
from datetime import datetime

import pytz
from django.contrib.contenttypes.models import ContentType
from django.db import migrations

BOOKMARK_MODELS = (
    ("DataSetBookmark", "dataset"),
    ("ReferenceDataSetBookmark", "reference_dataset"),
    ("VisualisationBookmark", "visualisation"),
)


def migrate_bookmark_created_dates(apps, _):
    """
    For all existing bookmarks:

    1. Try to find an associated event in the event log
    2. If an event was found, set the bookmark created date to the event timestamp
    3. If no event was found set the bookmark created date to 01/10/23 (when this event type was added)
    """
    eventlog_model = apps.get_model("eventlog", "EventLog")
    all_events = eventlog_model.objects.filter(event_type=51)
    default_event_date = datetime(2023, 10, 1, tzinfo=pytz.UTC)
    for model_name, foreign_key in BOOKMARK_MODELS:
        bookmark_model = apps.get_model("datasets", model_name)
        for bookmark in bookmark_model.objects.all():
            print(
                f"Attempting to find bookmark event for {model_name} "
                f"with id {bookmark.id} created at {bookmark.created_date}"
            )
            bookmarked_object = getattr(bookmark, foreign_key)
            matching_events = all_events.filter(
                user=bookmark.user,
                object_id=bookmarked_object.id,
                content_type_id=ContentType.objects.get_for_model(bookmarked_object).id,
            )
            if not matching_events.exists():
                print("No matching event found. Setting created to 1 Oct 2023")
                bookmark.created_date = default_event_date
            else:
                print(f"found {matching_events.count()} matching events")
                event = matching_events.latest("timestamp")
                print(f"Setting created to {event.timestamp}")
                bookmark.created_date = event.timestamp
            bookmark.save()


class Migration(migrations.Migration):
    dependencies = [
        ("datasets", "0159_auto_20231211_1053"),
    ]

    operations = [
        migrations.RunPython(migrate_bookmark_created_dates, migrations.RunPython.noop),
    ]