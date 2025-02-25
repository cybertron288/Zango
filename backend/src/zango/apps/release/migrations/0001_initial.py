# Generated by Django 4.2.11 on 2024-07-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=255)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(blank=True, editable=False, max_length=255)),
                ('version', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('initiated', 'Initiated'), ('in_progress', 'In Progress'), ('released', 'Released'), ('failed', 'Failed'), ('archived', 'Archived')], default='initiated', max_length=20)),
                ('last_git_hash', models.CharField(max_length=40)),
                ('release_result', models.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
