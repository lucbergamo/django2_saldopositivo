from django import forms
from core.models import GastoVariavel

class GastoVariavelForm(forms.ModelForm):
    class Meta:
        model = GastoVariavel
        fields = ['titulo', 'data_gasto', 'valor', 'tipo']