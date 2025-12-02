from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class GastoVariavel(models.Model):
    titulo = models.CharField(max_length=200)
    data_gasto = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    TIPOS = [
        ('alimentacao', 'Alimentação'),
        ('transporte', 'Transporte'),
        ('lazer', 'Lazer'),
        ('outros', 'Outros'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS)

    def __str__(self):
        return f"{self.titulo} - {self.valor}"

class GastoFixo(models.Model):
    titulo = models.CharField(max_length=200)
    criado = models.DateField(auto_created=True)
    dia_pagamento = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)],
        help_text="Dia do mês em que normalmente se paga este gasto (1 a 31).")
    
    bancoPagador = models.CharField(max_length=500)
    TIPOS = [
        ('Débito Automatico', 'Débito Automatico'),
        ('Pix', 'Pix'),
        ('Débito em Conta', 'Débito em Conta'),
        ('Cartão de Crédito', 'Cartão de Crédito'),
    ]
    formaPagamento = models.CharField(max_length=30, choices=TIPOS, blank=True, null=True)

    def __str__(self):
        return f"{self.titulo}" 

class RegistroGastoFixo(models.Model):
    gasto_fixo = models.ForeignKey(
        GastoFixo,
        on_delete=models.PROTECT,       # evita apagar um gasto enquanto há registros
        related_name='registros'
    )
    criado = models.DateField(auto_now_add=True)
    dataPagamento = models.DateField()
    valorPago = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.titulo} - {self.valorPago}"