from django.shortcuts import render
from .models import Car
from django.views.generic import ListView , DetailView , CreateView

# Create your views here.

class CarList(ListView):
    model = Car 

class CarDetail( DetailView):
    model = Car