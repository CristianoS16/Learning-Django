from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'João',
    })


def contato(request):
    return render(request, 'temp/temp.html')


def sobre(request):
    return HttpResponse("sobre")
