# Generated by Django 3.0.4 on 2020-04-01 02:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        verbose_name="date created",
                    ),
                ),
                (
                    "date_completed",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="date completed"
                    ),
                ),
                (
                    "player_1",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="player_1",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "player_2",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="player_2",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "winner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="winner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        )
    ]
