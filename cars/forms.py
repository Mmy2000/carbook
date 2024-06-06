from django import forms
from django.forms.models import inlineformset_factory
from .models import Car , CarImages , Model

class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['name']

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImages
        fields = ['car' , 'image']

CarImageFormset = inlineformset_factory(
    Car , 
    CarImages , 
    form = CarImageForm ,
    fields = ['image'],
    extra=4 , 
    can_delete=True,
)

class CarForm(forms.ModelForm):
    new_model = forms.CharField(required=False)
    existing_model = forms.ModelChoiceField(queryset=Model.objects.all(), required=False)


    class Meta:
        model = Car
        exclude = ('slug', 'owner', 'model')

    def clean(self):
        cleaned_data = super().clean()
        new_model = cleaned_data.get('new_model')
        existing_model = cleaned_data.get('existing_model')

        
        if new_model and existing_model:
            raise forms.ValidationError("Please enter either a new model or select an existing model, not both.")
        
        if not new_model and not existing_model:
            raise forms.ValidationError("Please provide a model.")

        
        return cleaned_data