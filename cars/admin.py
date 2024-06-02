from django.contrib import admin
from .models import Car , CarImages , Model
from django_summernote.admin import SummernoteModelAdmin
import admin_thumbnails


# Register your models here.
@admin_thumbnails.thumbnail('image')
class ProductGallaryInline(admin.TabularInline):
    model = CarImages
    extra = 1

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name' , 'total_price','model'  ,'owner']
    list_filter = ('name' , 'total_price' , 'model','owner','color')
    inlines = [ProductGallaryInline] 
admin.site.register(Car,SomeModelAdmin)
admin.site.register(CarImages)
admin.site.register(Model)