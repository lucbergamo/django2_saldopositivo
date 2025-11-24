from django.http import HttpResponse , request
from django.shortcuts import render, redirect, get_object_or_404
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

def edit_gastos_var(request, pk):
    editGasto = get_object_or_404(GastoVariavel, pk=pk)
    if request.method == 'POST':
        form = GastoVariavelForm(request.POST, instance=editGasto)
        if form.is_valid():
            form.save()
            return redirect('gastos_var_lista')
    else:
        return render(request, 'delete_gastos_var.html', {'form':form, 'edit_Gasto': editGasto})  

def delete_gastos_var(request):
   return render(request, 'teste_js.html')
   ''' deleteGasto = get_object_or_404(GastoVariavel)
    if request.method == 'POST':
        de.delete()
        return redirect('teste_js')
    else:'''
           