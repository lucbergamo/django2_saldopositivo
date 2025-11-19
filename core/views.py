from django.http import HttpResponse , request
from django.shortcuts import render, redirect
from .forms import GastoVariavelForm

def index(request):
    return render(request, 'index.html')

def gastos_var(request):
    if request.method == 'POST':
        form = GastoVariavelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gastos_var')
    else:
        form = GastoVariavelForm()
    return render(request, 'gastos_var.html', {'form':form})