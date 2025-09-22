from django.shortcuts import render
from clothes.models import Clothes
from django.views import generic


class AllClothesViews(generic.ListView):
    model = Clothes
    template_name = 'all_clothes.html'
    context_object_name = 'clothes'
    ordering = ['-id']

class ChildClothesViews(generic.ListView):
    model = Clothes
    template_name = 'child_clothes.html'
    context_object_name = 'clothes'
    ordering = ['-id']

class TeenClothesViews(generic.ListView):
    model = Clothes
    template_name = 'teen_clothes.html'
    context_object_name = 'clothes'
    ordering = ['-id']

class AdultClothesViews(generic.ListView):
    model = Clothes
    template_name = 'adult_clothes.html'
    context_object_name = 'clothes'
    ordering = ['-id']




