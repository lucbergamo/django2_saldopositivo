
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Gastos Variáveis
    path('gastos_var', views.gastos_var, name='gastos_var'), 
    path('gastos_var_lista', views.gastos_var_lista, name='gastos_var_lista'),
    path('edit_gastos_var/<int:pk>', views.edit_gastos_var, name='edit_gastos_var'),
    path('delete_gastos_var/<int:pk>', views.delete_gastos_var, name='delete_gastos_var'),

    # Gastos Fixos
    path('novo_gastos_fixo/', views.novo_gastos_fixo, name='novo_gastos_fixo'), 
    path('gastos_fixo_lista/', views.gastos_fixo_lista, name='gastos_fixo_lista'),
    path('edit_gastos_fixo/<int:pk>', views.edit_gastos_fixo, name='edit_gastos_fixo'),
    path('registro_gasto_fixo/', views.registro_gasto_fixo, name='registro_gasto_fixo')
]