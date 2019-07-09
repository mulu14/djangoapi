from rest_framework import serializers
from mortgage_request.models import MortgageRequest


class MortgageRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MortgageRequest
        fields = ('id', 'created', 'person_number_one', 'person_number_two', 'property_name_municipality')