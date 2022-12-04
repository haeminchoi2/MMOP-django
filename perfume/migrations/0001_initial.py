# Generated by Django 4.1.3 on 2022-12-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_id', models.IntegerField()),
                ('image', models.CharField(blank=True, max_length=256, null=True)),
                ('title', models.CharField(max_length=100)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=5, null=True)),
                ('price', models.FloatField(default=0)),
                ('launch_date', models.DateField(blank=True, null=True)),
                ('top_notes', models.TextField(blank=True, null=True)),
                ('heart_notes', models.TextField(blank=True, null=True)),
                ('base_notes', models.TextField(blank=True, null=True)),
                ('none_notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '향수',
                'verbose_name_plural': '향수 제품',
                'db_table': 'perfume',
                'ordering': ['-launch_date', 'brand', 'title'],
            },
        ),
    ]
