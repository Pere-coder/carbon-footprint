from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import EnergyUsageForm, TravelForm, FoodConsumptionForm, WasteManagementForm, SignUp
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def calculate_carbon_footprint(energy, travel, food, waste):
    energy_footprint = energy.electricity_kwh * 0.233 + energy.gas_kwh * 0.184 + energy.heating_oil_liters * 2.52
    travel_footprint = travel.car_miles * 0.27 + travel.public_transport_miles * 0.05 + travel.flights_hours * 90
    food_footprint = (food.meat_per_week * 27 + food.dairy_per_week * 13 + food.plant_based_per_week * 2)
    waste_footprint = waste.waste_kg * (1 - waste.recycling_percentage / 100) * 2.5
    total_footprint = energy_footprint + travel_footprint + food_footprint + waste_footprint
    return total_footprint


@login_required(login_url='/signup')
def footprint_calculator(request):
    if request.method == 'POST':
        energy_form = EnergyUsageForm(request.POST)
        travel_form = TravelForm(request.POST)
        food_form = FoodConsumptionForm(request.POST)
        waste_form = WasteManagementForm(request.POST)
        

        if all([energy_form.is_valid(), travel_form.is_valid(), food_form.is_valid(), waste_form.is_valid()]):
            energy_data = energy_form.save(commit=False)
            energy_data.created_by = request.user
            energy_data.save()
            travel_data = travel_form.save(commit=False)
            travel_data.created_by = request.user
            travel_data.save()
            food_data = food_form.save(commit=False)
            food_data.created_by = request.user
            food_data.save()
            waste_data = waste_form.save(commit=False)
            waste_data.created_by = request.user
            waste_data.save()
            carbon_footprint = calculate_carbon_footprint(energy_data, travel_data, food_data, waste_data)
            return render(request, 'calculator/results.html', {'carbon_footprint': carbon_footprint})
    else:
        energy_form = EnergyUsageForm()
        travel_form = TravelForm()
        food_form = FoodConsumptionForm()
        waste_form = WasteManagementForm()
        
    return render(request, 'calculator/calculator.html', {
                'energy_form': energy_form,
                'travel_form': travel_form,
                'food_form': food_form,
                'waste_form': waste_form,
            })


def signUp(request):
    if request.method == "POST":
        form = SignUp(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignUp()
    return render(request, 'signup.html', {'form': form})
        




