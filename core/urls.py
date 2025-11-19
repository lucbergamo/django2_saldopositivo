
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gastos_var', views.gastos_var, name='gastos_var'), 
]
