from django.shortcuts import render , redirect
from .models import Car , Model
from django.views.generic import ListView , DetailView , CreateView
from .filters import CarsFilter
from django_filters.views import FilterView
from django.urls import reverse
from .forms import CarForm , CarImageForm , CarImageFormset
from django.db.models.query_utils import Q

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
    

    
class AddListing(CreateView):
    model = Car
    form_class = CarForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_formset = CarImageFormset()
        return self.render_to_response(self.get_context_data(
            form=form,
            image_formset=image_formset,
        ))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        image_formset = CarImageFormset(self.request.POST, self.request.FILES)
        
        if form.is_valid() and image_formset.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            
            new_model = form.cleaned_data.get('new_model')
            existing_model = form.cleaned_data.get('existing_model')

            
            if new_model:
                model_instance, created = Model.objects.get_or_create(name=new_model)
                myform.model = model_instance
            else:
                myform.model = existing_model
            
            myform.save()
            
            for image_form in image_formset:
                myform2 = image_form.save(commit=False)
                myform2.car = myform
                myform2.save()
                
            ### send gmail message
            
            return redirect(reverse('car_list'))
        else:
            return self.render_to_response(self.get_context_data(
                form=form,
                image_formset=image_formset,
            ))