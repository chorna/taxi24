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


class Invoice(models.Model):
    STATE_CHOICES = [
        (1, 'Open'),
        (2, 'Paid')
    ]
    trip_id = models.ForeignKey(
        Trip,
        on_delete=models.PROTECT,
        db_column='trip_id'
        )
    serie = models.CharField(max_length=4)
    number = models.CharField(max_length=8)
    tax_amount = models.FloatField(default=0.00)
    base_amount = models.FloatField()

    @property
    def total_amount(self) -> float:
        return self.tax_amount + self.base_amount
