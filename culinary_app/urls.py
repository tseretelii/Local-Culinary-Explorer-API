from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'specialities', SpecialitiesViewSet)
router.register(r'chief', ChiefViewSet)
router.register(r'ingredients', IngridientsViewSet)
router.register(r'dishCategory', DishCategoryViewSet)
router.register(r'recipe', RecipeViewSet)
router.register(r'rate', RateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreationView.as_view()),
    path('login/', LoginView.as_view()),
]