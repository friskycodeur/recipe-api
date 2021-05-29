from rest_framework import serializers
from .models import Recipe,Tag,ingredient

#  Serializer class for Recipe
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['title','ingredients','procedure','author','time_to_make','tags']

#  Serializer class for Tags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['name']


# Serializer Class for ingredients
class ingredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=ingredient
        fields=['name']
