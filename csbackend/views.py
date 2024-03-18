from django.shortcuts import render
from rest_framework import generics
from .models import Countries
from .serializers import CountriesSerializer

# Create your views here.
class CountriesListCreate(generics.ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class CountriesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    lookup_field = 'primary_key'

