from django.shortcuts import render
from rest_framework import generics
from .models import Countries, States
from .serializers import CountriesSerializer, StatesSerializer

# Create your views here.
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





