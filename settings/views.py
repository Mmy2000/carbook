from django.shortcuts import render
from cars.models import Car
# Create your views here.
def home(request):
    car = Car.objects.all()
    return render(request , 'home.html')