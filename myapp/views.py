from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index (response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'myapp/list.html', {"ls":ls})

def home(response):
    return render(response, 'myapp/home.html', {})

def create(response):
    form = CreateNewList()
    return render(response, 'myapp/create.html',{"form":form})