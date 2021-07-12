# Generated by Django 3.2.5 on 2021-07-12 01:28

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_cab_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='cab',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point([0, 0]), srid=4326),
        ),
    ]
