from django.shortcuts import render
from .forms import EnergyUsageForm, TravelForm, FoodConsumptionForm, WasteManagementForm


def calculate_carbon_footprint(enery, travel, food, waste):
    energy_footprint = energy.electricity_kwh * 0.233 + energy.gas_kwh * 0.184 + energy.heating_oil_liters * 2.52
    travel_footprint = travel.car_miles * 0.27 + travel.public_transport_miles * 0.05 + travel.flights_hours * 90
    food_footprint = (food.meat_per_week * 27 + food.dairy_per_week * 13 + food.plant_based_per_week * 2)
    waste_footprint = waste.waste_kg * (1 - waste.recycling_percentage / 100) * 2.5
    total_footprint = energy_footprint + travel_footprint + food_footprint + waste_footprint
    return total_footprint


def footprint_calculator(request):
    if request.method == 'POST':
        energy_form = EnergyUsageForm(request.POST)
        travel_form = TravelForm(request.POST)
        food_form = FoodConsumptionForm(request.POST)
        waste_form = WasteManagementForm(request.POST)

        if all([energy_form.is_valid(), travel_form.is_valid(), food_form.is_valid(), waste_form.is_valid()]):
            energy_data = energy_form.save()
            travel_data = travel_form.save()
            food_data = food_form.save()
            waste_data = waste_form.save()

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