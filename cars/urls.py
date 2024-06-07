from django.urls import path
from . import views
urlpatterns = [
    path('' ,views.CarList.as_view() , name="car_list" ),
    path('carId=<int:pk>' ,views.CarDetail.as_view() , name="car_details" ),
    path( 'new/',views.AddListing.as_view() , name='car_new' ),
]