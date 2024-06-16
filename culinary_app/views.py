from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
# Create your views here.


class SpecialitiesViewSet(viewsets.ModelViewSet):
    queryset = Specialities.objects.all()
    serializer_class = SpecialitiesSerializer
    permission_classes = [IsAdminUser]

class ChiefViewSet(viewsets.ModelViewSet):
    queryset = Chief.objects.all()
    serializer_class = ChiefSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class IngridientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngridientsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DishCategoryViewSet(viewsets.ModelViewSet):
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer
    permission_classes = [IsAdminUser]

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserHasIngredientsViewSet(viewsets.ModelViewSet):
    queryset = UserHasIngredients.objects.all()
    serializer_class = UserHasIngredientsSerializer
    permission_classes = [IsAuthenticated]

# class UserSuggestionsViewSet(APIView):
#     def get(self, request):
#         user = request.user
#         Ingredients = serializers.serialize('json', UserHasIngredients.objects.filter(user = user))
#         Ingredients = Ingredients[0]['ingredients']
# #        suggestions = serializers.serialize('json', UserSuggestions.objects.filter(user = user))

#         return Response({"suggested-recipes": Ingredients}) Prefetch

# # Use select_related for single-valued relationships (foreign key, one-to-one)
# optimized_queryset = MyModel.objects.select_related('relatedmodel').all()

# # Use prefetch_related for multi-valued relationships (many-to-many, reverse foreign key)
# optimized_queryset = MyModel.objects.prefetch_related('manyrelatedmodel_set').all()



class UserCreationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists(): # if User.objects.get(username=username): ასე არა!
            return Response({"Response": "User allready Exists!"})
        
        user = User.objects.create_user(username=username, password=password)
        return Response({"Response": "User Created Successfully!"})
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username, password = password)
        if user:
            token, created = Token.objects.get_or_create(user = user) # აქ created არ უნდა გამომრჩეს
            return Response({"Token": token.key})
        return Response({"Response":"User Not Found!"})