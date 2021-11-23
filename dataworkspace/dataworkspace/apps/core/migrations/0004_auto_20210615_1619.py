# Generated by Django 3.2.4 on 2021-06-15 16:19

import uuid

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0003_usersatisfactionsurvey"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=256, unique=True)),
                ("schema_name", models.CharField(max_length=63, unique=True)),
            ],
            options={"verbose_name": "Team", "verbose_name_plural": "Teams"},
        ),
        migrations.CreateModel(
            name="TeamMembership",
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
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="memberships",
                        to="core.team",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_memberships",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("team_id", "user_id")}},
        ),
        migrations.AddField(
            model_name="team",
            name="member",
            field=models.ManyToManyField(
                through="core.TeamMembership", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
