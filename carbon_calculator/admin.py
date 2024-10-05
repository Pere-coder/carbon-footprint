from django.contrib import admin
from .models import EnergyUsage, Travel, FoodConsumption, WasteManagement
# Register your models here.

admin.site.register(EnergyUsage)
admin.site.register(Travel)
admin.site.register(FoodConsumption)
admin.site.register(WasteManagement)

