from django.contrib.gis.db import models as gis_models
from django.db import models

class Household(models.Model):
    applicant_name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    wheelchair_access_needed = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    school_age_children = models.PositiveIntegerField(default=0)
    preferred_counties = models.JSONField(default=list)
    preferred_towns = models.JSONField(default=list)
    needs_public_transport = models.BooleanField(default=False)
    needs_specific_facilities = models.CharField(max_length=100, blank=True)
    needs_adaptations = models.BooleanField(default=False)
    years_on_list = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.applicant_name} ({self.size} ppl)"

class VacantHouse(models.Model):
    address = models.CharField(max_length=255)
    county = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    bedrooms = models.PositiveIntegerField()
    wheelchair_accessible = models.BooleanField(default=False)
    pet_friendly = models.BooleanField(default=False)
    near_public_transport = models.BooleanField(default=False)
    nearby_schools = models.BooleanField(default=False)

    def __str__(self):
        return self.address
