from django import forms
from core.models import GastoVariavel, GastoFixo, RegistroGastoFixo, ReceitaFixa, RegistroReceitaFixa

class GastoVariavelForm(forms.ModelForm):
    class Meta:
        model = GastoVariavel
        fields = ['titulo', 'data_gasto', 'valor', 'tipo']
        

        widgets = {
            'data_gasto': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',  # integra com Bootstrap
                    # 'placeholder': 'Selecione a data', # opcional
                },
                format='%Y-%m-%d'  # formato aceito pelo input date
            )
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
        
        widgets = {
            'dataRecebimento': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',  # integra com Bootstrap
                    # 'placeholder': 'Selecione a data', # opcional
                },
                format='%Y-%m-%d'  # formato aceito pelo input date
            )
        }
                       


class RegistroReceitaFixaForm(forms.ModelForm):
    class Meta:
        model = RegistroReceitaFixa
        fields = ['receita_fixa', 'dataRecebimento','valor']
