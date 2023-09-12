from django.db import models

# Create your models here.

# creating category model
class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# creating drug item model
class drugItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits= 5, decimal_places=2)
    inStock = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.name