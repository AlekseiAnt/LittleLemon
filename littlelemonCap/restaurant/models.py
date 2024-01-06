from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=11, decimal_places=0)
    name = models.CharField(max_length=255)
    no_of_guests = models.DecimalField(max_digits=6, decimal_places=0)
    bookingDate = models.DateTimeField()

class Menu(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=11, decimal_places=0)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.DecimalField(max_digits=5, decimal_places=0)