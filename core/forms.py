from django import forms
from core.models import GastoVariavel, GastoFixo, RegistroGastoFixo, ReceitaFixa

class GastoVariavelForm(forms.ModelForm):
    class Meta:
        model = GastoVariavel
        fields = ['titulo', 'data_gasto', 'valor', 'tipo']

        # 1. Definir o widget para o campo data_gasto
        widgets = {
            'data_gasto': forms.DateInput(attrs={
                # Essa classe 'datepicker' será usada pelo JavaScript
                'class': 'form-control datepicker', 
                'type': 'text' # Importante: Define como 'text' para que o navegador não use o datepicker nativo
            })
        }


class RegistroGastoFixoForm(forms.ModelForm):
    class Meta:
        model = RegistroGastoFixo
        fields = ['gasto_fixo', 'dataPagamento', 'valorPago']


class GastoFixoForm(forms.ModelForm):
    class Meta:
        model = GastoFixo
        fields = ['titulo', 'dia_pagamento','formaPagamento', 'bancoPagador', 'criado']

class ReceitaFixaForm(forms.ModelForm):
    class Meta:
        model = ReceitaFixa
        fields = ['titulo', 'dataRecebimento','receitaEsperada', 'bancoRecebedor']
