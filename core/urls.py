
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gastos_var', views.gastos_var, name='gastos_var'), 
    path('gastos_var_lista', views.gastos_var_lista, name='gastos_var_lista')
]
