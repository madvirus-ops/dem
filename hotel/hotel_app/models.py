from django.db import models

# Create your models here.

class HotelData(models.Model):
    room_number = models.IntegerField()
    amount_paid = models.IntegerField()
    occupant_name = models.CharField(max_length=254)
    occupant_email = models.EmailField(max_length=254)
    occupant_occupation = models.CharField(max_length=50)
    number_night = models.IntegerField()
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=60)
    
    def __str__(self):
         return self.occupant_name

     

