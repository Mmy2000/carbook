from django.shortcuts import render , redirect
from .models import Car , Model
from django.views.generic import ListView , DetailView , CreateView,UpdateView
from .filters import CarsFilter
from django_filters.views import FilterView
from django.urls import reverse
from .forms import CarForm , CarImageForm , CarImageFormset
from django.db.models.query_utils import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
    

class AddListing(LoginRequiredMixin,CreateView):
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
            messages.success(request, ' Your Car added successfully')
            return redirect(reverse('car_list'))
        else:
            return self.render_to_response(self.get_context_data(
                form=form,
                image_formset=image_formset,
            ))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Add'  # Add an action context variable for template differentiation
        return context

@login_required(login_url='login') 
def deleteCar(request , id):
    car = Car.objects.get(id=id)
    car.delete()
    messages.success(request, ' Your Car deleted successfully')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class UpdateListing(LoginRequiredMixin,UpdateView):
    model = Car
    form_class = CarForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_formset = CarImageFormset(instance=self.object)

        # Ensure the model field is populated correctly
        if self.object.model:
            form.fields['existing_model'].initial = self.object.model

        return self.render_to_response(self.get_context_data(
            form=form,
            image_formset=image_formset,
        ))
    

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        image_formset = CarImageFormset(self.request.POST, self.request.FILES, instance=self.object)
        
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
            
            # Save formset data
            images = image_formset.save(commit=False)
            for image in images:
                image.car = myform
                image.save()

            # Delete images not in formset
            for image in image_formset.deleted_objects:
                image.delete()
                
            ### send gmail message
            messages.success(request, ' Your Car updated successfully')
            return redirect(reverse('car_list'))
        else:
            return self.render_to_response(self.get_context_data(
                form=form,
                image_formset=image_formset,
            ))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'  # Add an action context variable for template differentiation
        return context