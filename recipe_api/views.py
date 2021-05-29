from django.shortcuts import render, resolve_url
from django.http import HttpResponse
# Create your views here.
from .models import Recipe,Tag,ingredient
from rest_framework.response import Response
from .serializers import RecipeSerializer,TagSerializer,ingredientSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class TagViewset(viewsets.ModelViewSet):
    serializer_class=TagSerializer
    queryset=Tag.objects.all()

class RecipeViewset(viewsets.ModelViewSet):
    serializer_class=RecipeSerializer
    queryset=Recipe.objects.all()

class ingredientViewset(viewsets.ModelViewSet):
    serializer_class=ingredientSerializer
    queryset=ingredient.objects.all()
