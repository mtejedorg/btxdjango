from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.TextField(default="UnknownName")
    price = models.FloatField(default=0.0)
    custom_label_0 = models.FloatField(default=0.0)
    discount = models.FloatField(default=0.0)
    type = models.TextField(default = "Unknown Type")

    def __str__(self):
        return self.name
