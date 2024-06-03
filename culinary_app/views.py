from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.


class SpecialitiesViewSet(viewsets.ModelViewSet):
    queryset = Specialities.objects.all()
    serializer_class = SpecialitiesSerializer

class ChiefViewSet(viewsets.ModelViewSet):
    queryset = Chief.objects.all()
    serializer_class = ChiefSerializer

class IngridientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngridientsSerializer

class DishCategoryViewSet(viewsets.ModelViewSet):
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
