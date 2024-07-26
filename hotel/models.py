from django.db import models

class Second(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Order(models.Model):
    hotel = models.ForeignKey('Second', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Removed default value
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.hotel.name} - {self.quantity}"







