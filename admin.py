from django.contrib import admin
from .models import Household, VacantHouse

@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'size', 'wheelchair_access_needed', 'pets')

@admin.register(VacantHouse)
class VacantHouseAdmin(admin.ModelAdmin):
    list_display = ('address', 'county', 'town', 'bedrooms', 'wheelchair_accessible')
