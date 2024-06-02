import django_filters
from .models import Car

class CarsFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = ['name', 'model', 'total_price','year','color' ]