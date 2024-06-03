from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Specialities(models.Model):
    specialty = models.CharField(max_length=50) # Personal chef, Pastry chef, Sous chef, Head Chef etc.

    def __str__(self):
        return self.specialty


class Chief(models.Model):
    name =          models.CharField(max_length=100)
    surname =       models.CharField(max_length=100)
    speciality =    models.ForeignKey(Specialities, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    ingredients = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredients


class DishCategory(models.Model):
    dish_category = models.CharField(max_length=50) # starter, main, etc.

    def __str__(self):
        return self.dish_category


class Recipe(models.Model):
    name =          models.CharField(max_length=100)
    description =   models.TextField()
    ingredients =   models.ManyToManyField(Ingredients)
    dish_category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    preparation =   models.TextField()

    def __str__(self):
        return self.name


class Rate(models.Model):                                               
    recipe =        models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user =          models.ForeignKey(User, on_delete=models.CASCADE)         # Rating By Each User On A Recipe
    rating =        models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.recipe
    
    class Meta:
        unique_together = ('recipe', 'user')