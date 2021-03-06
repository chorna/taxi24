# Generated by Django 3.2.5 on 2021-07-11 03:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=40, null=True)),
                ('model', models.CharField(blank=True, max_length=40, null=True)),
                ('number_plate', models.CharField(max_length=10, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cab',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('state', models.IntegerField(choices=[(0, 'Not Available'), (1, 'Available')], default=1)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('driver_id', models.ForeignKey(db_column='driver_id', on_delete=django.db.models.deletion.PROTECT, to='drivers.driver')),
                ('vehicle_id', models.ForeignKey(db_column='vehicle_id', on_delete=django.db.models.deletion.PROTECT, to='drivers.vehicle')),
            ],
        ),
    ]
