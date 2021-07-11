import uuid

from django.db import models

from customers.models import Customer
from drivers.models import Cab

# Create your models here.


class RequestTrip(models.Model):
    """
        Model for registering request of cabs
    """
    STATE_CHOICES = [
        (0, 'Cancel'),
        (1, 'Waiting'),
        (2, 'Accepted'),
    ]
    customer_id = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        db_column='customer_id',
    )
    cab_id = models.ForeignKey(
        Cab,
        on_delete=models.PROTECT,
        db_column='cab_id',
    )
    # TODO: locations
    state = models.IntegerField(choices=STATE_CHOICES, default=1)
    created_date = models.DateTimeField(auto_now_add=True)


class Trip(models.Model):
    """
        Model for registering trip of Customers
    """
    STATE_CHOICES = [
        (1, 'Paused'),
        (2, 'Active'),
        (3, 'Finished')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request_id = models.ForeignKey(
        RequestTrip,
        on_delete=models.PROTECT,
        db_column='request_id',
    )
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    price = models.FloatField()
    state = models.IntegerField(choices=STATE_CHOICES, default=2)
