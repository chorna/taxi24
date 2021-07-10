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
    document_number = models.CharField(max_length=15)
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


