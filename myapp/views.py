from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index (response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'myapp/list.html', {"ls":ls})

def home(response):
    return render(response, 'myapp/home.html', {})

def test(response):
    t = Item.objects.get(id=1)
    return render(response, 'myapp/testpage.html',{"t":t})