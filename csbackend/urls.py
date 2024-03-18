from django.urls import path
from . import views 

urlpatterns = [
    path('countries/', views.CountriesListCreate.as_view(), name='countries-view-create'),
    path('countries/<int:pk>/', views.CountriesRetrieveUpdateDestroy.as_view(), name='update')
]