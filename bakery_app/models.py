from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=1)
    description = models.TextField()
    specifications = models.TextField()
    reviews = models.IntegerField(default=0)
    image = models.ImageField(upload_to='cake_images/')  # Add this line for the image field

    def __str__(self):
        return self.name


