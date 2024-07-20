from rest_framework import serializers
from .models import *

class SpecialitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialities
        fields = '__all__'

class ChiefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chief
        fields = '__all__'

class IngridientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCategory
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class RateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        model = Rate
        fields = '__all__'


class UserHasIngredientsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        model = UserHasIngredients
        fields = '__all__'


# class UserSuggestionsSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(serializers.CurrentUserDefault())

#     class Meta:
#         model = UserSuggestions
#         fields = '__all__'