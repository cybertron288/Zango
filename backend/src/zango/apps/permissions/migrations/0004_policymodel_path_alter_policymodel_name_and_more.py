# Generated by Django 4.2.10 on 2024-02-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("permissions", "0003_default_policy"),
    ]

    operations = [
        migrations.AddField(
            model_name="policymodel",
            name="path",
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name="Policy path"),
        ),
        migrations.AlterField(
            model_name="policymodel",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Name of the policy"),
        ),
        migrations.AlterUniqueTogether(
            name="policymodel",
            unique_together={("name", "path")},
        ),
    ]
