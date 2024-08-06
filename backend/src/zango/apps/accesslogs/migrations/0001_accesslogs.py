# Generated by Django 4.2.11 on 2024-04-12 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("appauth", "0006_appusermodel_app_objects"),
    ]

    operations = [
        migrations.CreateModel(
            name="AppAccessLog",
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
                (
                    "user_agent",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="User Agent"
                    ),
                ),
                (
                    "ip_address",
                    models.GenericIPAddressField(
                        db_index=True, null=True, verbose_name="IP Address"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        db_index=True,
                        max_length=255,
                        null=True,
                        verbose_name="Username",
                    ),
                ),
                (
                    "http_accept",
                    models.CharField(max_length=1025, verbose_name="HTTP Accept"),
                ),
                ("path_info", models.CharField(max_length=255, verbose_name="Path")),
                (
                    "attempt_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Attempt Time"
                    ),
                ),
                ("attempt_type", models.CharField(max_length=20, null=True)),
                ("is_login_successful", models.BooleanField(default=False)),
                ("session_expired_at", models.DateTimeField(blank=True, null=True)),
                (
                    "role",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appauth.userrolemodel",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appauth.appusermodel",
                    ),
                ),
            ],
            options={
                "ordering": ["-attempt_time"],
                "abstract": False,
            },
        ),
    ]
