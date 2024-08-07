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
from django.db.models import Count
import random
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

class UserSuggestionsViewSet(APIView):
    def get(self, request):
        try:
            user = User.objects.get(username=request.user)
            user_ingredients = UserHasIngredients.objects.get(user=user).ingredients.all()
            user_ingredient_ids = user_ingredients.values_list('id', flat=True)

            recipes = Recipe.objects.annotate(
                ingredient_count=Count('ingredients')
            ).filter(
                ingredients__in=user_ingredient_ids
            ).annotate(
                matched_ingredients=Count('ingredients', filter=models.Q(ingredients__in=user_ingredient_ids))
            ).filter(
                ingredient_count=models.F('matched_ingredients')
            )

            if recipes.exists():
                suggested_recipe = random.choice(list(recipes))
                suggested_recipe_json = serializers.serialize('json', [suggested_recipe])
                return Response({"suggestion":suggested_recipe_json})
            else:
                return Response({"response": "recipe doesn't exist"})

        except User.DoesNotExist:
            return Response({"response": "user doesn't exist"})




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