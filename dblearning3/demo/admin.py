from django.contrib import admin
from .models import Weather,Author
# Register your models here

class WeatherAdmin(admin.ModelAdmin):
    fields = ['cityName','temperature']
    
admin.site.register(Weather)
admin.site.register(Author)