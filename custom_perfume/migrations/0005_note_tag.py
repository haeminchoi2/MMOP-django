# Generated by Django 4.1.3 on 2022-12-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_perfume', '0004_alter_customperfume_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.TextField(blank=True, null=True),
        ),
    ]
