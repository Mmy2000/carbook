from django.contrib import admin
from .models import Car , CarImages , Model
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name' , 'total_price','model'  ,'owner']
admin.site.register(Car,SomeModelAdmin)
admin.site.register(CarImages)
admin.site.register(Model)