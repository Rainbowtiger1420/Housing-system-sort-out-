from django.core.management.base import BaseCommand
from housing.models import Household, VacantHouse

class Command(BaseCommand):
    help = 'Simple match households to houses by bedrooms >= size'

    def handle(self, *args, **kwargs):
        for hh in Household.objects.all():
            house = VacantHouse.objects.filter(bedrooms__gte=hh.size).first()
            if house:
                self.stdout.write(self.style.SUCCESS(f"Matched {hh} to {house.address}"))