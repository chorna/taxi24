from django.db import models

from drivers.models import Person

# Create your models here.


class CustomerCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Customer(Person):
    """
        Model for registering customer
    """
    category_id = models.ForeignKey(
        CustomerCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='category_id',
    )
    email = models.EmailField(null=True, blank=True)
