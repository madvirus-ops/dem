from django.shortcuts import render
from .models import HotelData
from django.contrib import messages



# Create your views here.

def register(request):
    if request.method == 'POST':
        room_number = request.POST['room_number']
        amount_paid = request.POST['amount_paid']
        occupant_name = request.POST['name']
        occupant_email = request.POST['email']
        occupant_occupation = request.POST['occupation']
        number_night = request.POST['number_of_nights']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        hotel_data = HotelData(room_number=room_number, amount_paid=amount_paid, occupant_name=occupant_name, occupant_email=occupant_email, occupant_occupation=occupant_occupation, number_night=number_night, start_date=start_date, end_date=end_date)
        hotel_data.save()
        messages.success(request,"Record stored succesfully")
        return render(request, 'hotel_app/register.html')
    else:
        return render(request, 'hotel_app/register.html')
        