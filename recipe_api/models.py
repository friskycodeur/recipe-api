from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ingredient(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title=models.CharField(max_length=200)
    ingredients=models.ManyToManyField('ingredient')
    procedure=models.TextField()
    author=models.OneToOneField(User, blank=True,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    time_to_make=models.IntegerField(default=0)
    tags=models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

