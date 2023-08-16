# Generated by Django 4.2.2 on 2023-08-07 05:34

from django.db import migrations
import django.db.models.deletion
import zelthy.backend.apps.tenants.dynamic_models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appauth', '0007_userrolemodel_temp_field'),        
        ('dynamic_models', '0005_programmodel_programapplicationvalidator'),
        
    ]

    operations = [
        migrations.AddField(
            model_name='framesmodel',
            name='user_role_fk',
            field=zelthy.backend.apps.tenants.dynamic_models.fields.ZForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appauth.userrolemodel'),
        ),
    ]
