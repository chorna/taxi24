# Generated by Django 3.2.5 on 2021-07-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20210711_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='state',
            field=models.IntegerField(choices=[(1, 'Paused'), (2, 'Active'), (3, 'Finished')], default=2),
        ),
    ]
