from django.urls import path
from . import views 


urlpatterns = [
    path('signup' , views.signup , name='signup'),
    path('profile/' , views.profile , name='profile'),
    path('mycars/' , views.myCars , name='my_cars'),
    path('profile/edit' , views.edit_profile , name='edit_profile'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),

]