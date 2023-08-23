from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'MeuApp/home.html')

def about(request):
    return render(request, 'MeuApp/about.html')

def pagina3(request):
    return render(request, "MeuApp/pagina3.html")

def index(request):
    return render(request, 'MeuApp/index.html')