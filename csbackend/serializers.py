from rest_framework import serializers
from .models import Countries, States

# Countries

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['id', 'code', 'name']
    


# States
        
class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ['id', 'code', 'name', 'countryId']
