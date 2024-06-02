from django.shortcuts import render
from .models import Car
from django.views.generic import ListView , DetailView , CreateView
from .filters import CarsFilter
from django_filters.views import FilterView


# Create your views here.

class CarList(FilterView):
    model = Car 
    paginate_by = 6
    filterset_class = CarsFilter
    template_name = 'cars/car_list.html'

class CarDetail( DetailView):
    model = Car

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Car.objects.filter(model=self.get_object().model)[:3]
        return context