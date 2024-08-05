# Generated by Django 4.2.2 on 2023-08-13 04:09

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import zango.apps.appauth.models
import zango.core.storage_utils


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("permissions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserRoleModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.CharField(blank=True, editable=False, max_length=255),
                ),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "modified_by",
                    models.CharField(blank=True, editable=False, max_length=255),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="Unique Name of the User Role",
                    ),
                ),
                ("config", models.JSONField(blank=True, null=True)),
                ("temp_field", models.CharField(max_length=20, null=True)),
                ("is_default", models.BooleanField(default=False)),
                (
                    "policies",
                    models.ManyToManyField(
                        blank=True,
                        related_name="role_policies",
                        to="permissions.policymodel",
                    ),
                ),
                (
                    "policy_groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="role_policy_groups",
                        to="permissions.policygroupmodel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, zango.apps.permissions.mixin.PermissionMixin),
        ),
        migrations.CreateModel(
            name="AppUserModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.CharField(blank=True, editable=False, max_length=255),
                ),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "modified_by",
                    models.CharField(blank=True, editable=False, max_length=255),
                ),
                (
                    "name",
                    models.CharField(max_length=75, verbose_name="full name of user"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined"),
                ),
                (
                    "address_line_1",
                    models.CharField(blank=True, max_length=255, verbose_name="address line 1"),
                ),
                (
                    "address_line_2",
                    models.CharField(blank=True, max_length=255, verbose_name="address line 2"),
                ),
                (
                    "address_line_3",
                    models.CharField(blank=True, max_length=255, verbose_name="address line 3"),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=100, verbose_name="city"),
                ),
                (
                    "state",
                    models.CharField(blank=True, max_length=255, verbose_name="state"),
                ),
                (
                    "pincode",
                    models.CharField(blank=True, max_length=20, verbose_name="pincode/zipcode"),
                ),
                (
                    "country",
                    models.CharField(max_length=200, null=True, verbose_name="country"),
                ),
                (
                    "profile_pic",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=zango.core.storage_utils.RandomUniqueFileName,
                        verbose_name="user profile pic",
                    ),
                ),
                ("extra_data", models.JSONField(null=True)),
                (
                    "policies",
                    models.ManyToManyField(related_name="user_policies", to="permissions.policymodel"),
                ),
                (
                    "policy_groups",
                    models.ManyToManyField(
                        related_name="user_policy_groups",
                        to="permissions.policygroupmodel",
                    ),
                ),
                ("roles", models.ManyToManyField(to="appauth.userrolemodel")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="app_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, zango.apps.permissions.mixin.PermissionMixin),
        ),
    ]
