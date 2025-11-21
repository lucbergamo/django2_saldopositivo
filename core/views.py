from django.http import HttpResponse , request
from django.shortcuts import render, redirect
from .forms import GastoVariavelForm
from .models import GastoVariavel

def index(request):
    return render(request, 'index.html')

def gastos_var_lista(request):
    gastos_variaveis = GastoVariavel.objects.all().order_by('data_gasto')
    context = {"gastos_var_todos": gastos_variaveis}
    return render(request, 'gastos_var lista.html', context)

def gastos_var(request):
    if request.method == 'POST':
        form = GastoVariavelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gastos_var')
    else:
        form = GastoVariavelForm()
    return render(request, 'gastos_var.html', {'form':form})