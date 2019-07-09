from django.db import models

# Create your models here.
class MortgageRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    person_number_one = models.CharField(max_length=100, blank=True, default='')
    person_number_two = models.CharField(max_length=100, blank=True, default='')
    property_name_municipality = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ('created',)