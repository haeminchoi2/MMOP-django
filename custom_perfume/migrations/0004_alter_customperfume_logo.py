# Generated by Django 4.1.3 on 2022-12-14 05:32

import custom_perfume.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_perfume', '0003_alter_customperfume_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customperfume',
            name='logo',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=custom_perfume.models.upload_to_custom_perfume_logo),
        ),
    ]
