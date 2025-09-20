from django.shortcuts import render
from clothes.models import Clothes

def all_clothes(request):
    if request.method == 'GET':
        clothes = Clothes.objects.all().order_by('-id')
        context = {
            'clothes': clothes,
        }
    return render(request, 'all_clothes.html', context=context)

def child_clothes(request):
    if request.method == 'GET':
        clothes = Clothes.objects.filter(tags__name='#Детскаяодежда').order_by('-id')
        context = {
            'clothes': clothes,
        }
    return render(request, 'child_clothes.html', context=context)

def teen_clothes(request):
    if request.method == 'GET':
        clothes = Clothes.objects.filter(tags__name='#Подростковаяодежда').order_by('-id')
        context = {
            'clothes': clothes,
        }
    return render(request, 'teen_clothes.html', context=context)

def adult_clothes(request):
    if request.method == 'GET':
        clothes = Clothes.objects.filter(tags__name='#Взрослаяодежда').order_by('-id')
        context = {
            'clothes': clothes,
        }
    return render(request, 'adult_clothes.html', context=context)


