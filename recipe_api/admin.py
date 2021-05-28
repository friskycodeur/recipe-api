from django.contrib import admin
from .models import Recipe,Tag,ingredient
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(ingredient)