from django.http import HttpResponse , request
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GastoVariavelForm, GastoFixoForm, RegistroGastoFixoForm, ReceitaFixaForm
from .models import GastoVariavel, GastoFixo, ReceitaFixa

def index(request):
    return render(request, 'index.html')


# ================    GASTOS VARIAVEIS ====================================
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
        form = GastoVariavelForm(instance=editGasto)
        return render(request, 'edit_gastos_var.html', {'form':form, 'edit_Gasto': editGasto})  

def excluir_gasto(pk):
    gasto = GastoVariavel.objects.get(id=pk)
    gasto.delete()
    

def delete_gastos_var(request, pk):
    if request.method == 'POST':
        resultado = excluir_gasto(pk)
        return redirect('gastos_var_lista')

# ===================    GASTOS FIXOS ====================================
def novo_gastos_fixo(request):
    if request.method == 'POST':
        form = GastoFixoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gastos_fixo_lista')
    else:
        form = GastoFixoForm()
        return render(request, 'novo_gastos_fixo.html', {'form':form})
    
def gastos_fixo_lista(request):
    gastos_fixos = GastoFixo.objects.all().order_by('dia_pagamento')
    context = {"gastos_fixos_todos": gastos_fixos}
    return render(request, 'gastos_fixo_lista.html', context)

def edit_gastos_fixo(request,pk):
    editGastoFixo = get_object_or_404(GastoFixo, pk=pk)
    if request.method == 'POST':
        form = GastoFixoForm(request.POST, instance=editGastoFixo)
        if form.is_valid():
            form.save()
            return redirect('gastos_fixo_lista')
    else:
        form = GastoFixoForm(instance=editGastoFixo)
        return render(request, 'edit_gastos_fixo.html', {'form':form, 'edit_Gasto': editGastoFixo}) 
     
def registro_gasto_fixo(request):
    if request.method == 'POST':
        form = RegistroGastoFixoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_gasto_fixo')
    else:
        form = RegistroGastoFixoForm()
    return render(request, 'registro_gasto_fixo.html', {'form':form})

# ================ RECEITAS FIXAS ==========================================
def novo_rec_fixa(request):
    if request.method == 'POST':
        form = ReceitaFixaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('novo_rec_fixa')
    else:
        form = ReceitaFixaForm()
    return render(request, 'novo_rec_fixa.html', {'form':form})
