# Generated by Django 4.2.2 on 2023-07-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=255)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(blank=True, editable=False, max_length=255)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name of the policy')),
                ('description', models.CharField(max_length=300, unique=True, verbose_name='Description of the policy')),
                ('config', models.JSONField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]