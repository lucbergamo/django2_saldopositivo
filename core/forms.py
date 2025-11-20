from django import forms
from core.models import GastoVariavel

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