# Generated by Django 4.1.2 on 2022-11-10 14:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("coachs", "0001_initial"),
        ("championships", "0001_initial"),
        ("stadiums", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("mascot", models.CharField(max_length=150)),
                ("team_foundation_year", models.DateField()),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "championship",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teams",
                        to="championships.championship",
                    ),
                ),
                (
                    "coach",
                    models.OneToOneField(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="current_team",
                        to="coachs.coach",
                    ),
                ),
                (
                    "stadium",
                    models.OneToOneField(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_owner",
                        to="stadiums.stadium",
                    ),
                ),
            ],
        ),
    ]
