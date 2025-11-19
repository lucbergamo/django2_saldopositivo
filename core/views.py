from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def gastos_var(request):
    return render(request, 'gastos_var.html')