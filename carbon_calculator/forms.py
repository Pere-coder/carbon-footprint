from django import forms
from .models import EnergyUsage, Travel, FoodConsumption, WasteManagement
from django.contrib.auth.models import User

class EnergyUsageForm(forms.ModelForm):
    class Meta:
        model = EnergyUsage
        fields = ['electricity_kwh', 'gas_kwh', 'heating_oil_liters']

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ['car_miles', 'public_transport_miles', 'flights_hours']
        
class FoodConsumptionForm(forms.ModelForm):
    class Meta:
        model = FoodConsumption
        fields = ['meat_per_week', 'dairy_per_week', 'plant_based_per_week']

class WasteManagementForm(forms.ModelForm):
    class Meta:
        model = WasteManagement
        fields = ['waste_kg', 'recycling_percentage'] 

class SignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        