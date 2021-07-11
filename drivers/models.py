import uuid

from django.db import models

# Create your models here.


class DocumentType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Person(models.Model):
    GENER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document_type_id = models.ForeignKey(
        DocumentType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='document_type_id',
    )
    document_number = models.CharField(max_length=15, unique=True)
    gener = models.CharField(choices=GENER_CHOICES,
                             max_length=1, null=True, blank=True)
    active = models.BooleanField(default=True)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        abstract = True


class Driver(Person):
    """
        Model for registering drivers
    """
    age = models.PositiveIntegerField(null=True, blank=True)


class Vehicle(models.Model):
    """
        Model for registering vehicles
    """
    brand = models.CharField(max_length=40, null=True, blank=True)
    model = models.CharField(max_length=40, null=True, blank=True)
    number_plate = models.CharField(max_length=10, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.number_plate}"


class Cab(models.Model):
    """
        Model for registering cabs
    """
    STATE_CHOICES = [
        (0, 'Not Available'),
        (1, 'Available'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    driver_id = models.ForeignKey(
        Driver,
        on_delete=models.PROTECT,
        db_column='driver_id',
    )
    vehicle_id = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        db_column='vehicle_id',
    )
    state = models.IntegerField(choices=STATE_CHOICES, default=1)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    # TODO: locations fields
