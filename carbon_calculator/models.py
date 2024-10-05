from django.db import models

# Create your models here.
class EnergyUsage(models.Model):
    electricity_kwh = models.FloatField(help_text="Electricity usage in kwh")
    gas_kwh = models.FloatField(help_text='Gas usage in KWh')
    heating_oil_liters = models.FloatField(help_text="Heating oil usage in liters")


class Travel(models.Model):
    car_miles = models.FloatField(help_text="Distance traveled by car (miles)")
    public_transport_miles = models.FloatField(help_text="Distance traveled by public transport (miles)")
    flights_hours = models.FloatField(help_text="Hours spent on flights")

class FoodConsumption(models.Model):
    meat_per_week = models.FloatField(help_text="Meat consumption per week (kg)")
    dairy_per_week = models.FloatField(help_text="Dairy consumption per week (kg)")
    plant_based_per_week = models.FloatField(help_text="Plant-based food consumption per week (kg)")


class WasteManagement(models.Model):
    waste_kg = models.FloatField(help_text="Amount of waste produced (kg)")
    recycling_percentage = models.FloatField(help_text="Percentage of waste recycled (%)")
    