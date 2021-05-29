from django.urls import path,include
from .views import RecipeViewset,TagViewset, ingredientViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('tag',TagViewset,basename='tag')
router.register('ingredient',ingredientViewset,basename='ingredient')
router.register('recipe',RecipeViewset,basename='recipe')

urlpatterns = [
    path('',include(router.urls)),
]