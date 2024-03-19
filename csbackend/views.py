from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Countries, States
from .serializers import CountriesSerializer, StatesSerializer

# Create your views here.
class CountryStateList(APIView):
    def get(self, request, country_code):
        """ country = Countries.objects.get(code=country_code)
        states = States.objects.filter(countryId=country.pk) """
        #states = States.objects.filter(countryId=country.id)
        states = States.objects.filter(countryId__code=country_code)
        serializer = StatesSerializer(states, many=True)
        return Response(serializer.data)


class CountriesListCreate(generics.ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class StatesListCreate(generics.ListCreateAPIView):
    queryset = States.objects.all()
    serializer_class = StatesSerializer


class CountriesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class StatesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = States.objects.all()
    serializer_class = StatesSerializer





