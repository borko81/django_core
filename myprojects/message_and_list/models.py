from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    name_lat = models.CharField(max_length=120, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    summary = models.TextField()
    feuture = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
