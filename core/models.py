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
    dia_pagamento = models.IntegerField(verbose_name='Dia do Pagamento', validators=[MinValueValidator(1), MaxValueValidator(31)],
        help_text="Dia do mês em que normalmente se paga este gasto (1 a 31).")
    
    bancoPagador = models.CharField(max_length=500, verbose_name='Banco que recebe o pagamento')
    TIPOS = [
        ('Débito Automatico', 'Débito Automatico'),
        ('Pix', 'Pix'),
        ('Débito em Conta', 'Débito em Conta'),
        ('Cartão de Crédito', 'Cartão de Crédito'),
    ]
    formaPagamento = models.CharField(max_length=30, choices=TIPOS, blank=True, null=True, verbose_name='Forma de Pagamento')

    def __str__(self):
        return f"{self.titulo}" 

class RegistroGastoFixo(models.Model):

    gasto_fixo = models.ForeignKey(
        GastoFixo,
        on_delete=models.PROTECT,       # evita apagar um gasto enquanto há registros
        related_name='registros', 
        verbose_name='Gasto Fixo'
    )
    criado = models.DateField(auto_now_add=True)
    dataPagamento = models.DateField(verbose_name='Data do Programada do pagamento')
    valorPago = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Pago')

    def __str__(self):
        return f"{self.titulo} - {self.valorPago}"
    
class ReceitaFixa(models.Model):
    titulo = models.CharField(max_length=80, verbose_name='Título')
    dataRecebimento = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)], verbose_name='Data de Recebimento',
        help_text="Dia do mês em que normalmente se paga este gasto (1 a 31).")
    receitaEsperada = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Receita Esperada')
    bancoRecebedor = models.CharField(max_length=50, verbose_name='Banco Recebedor')
 #   criado = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo}" 

class RegistroReceitaFixa(models.Model):
    receita_fixa = models.ForeignKey(
        ReceitaFixa,
        on_delete=models.PROTECT,       # evita apagar um gasto enquanto há registros
        related_name='registros', verbose_name='Receita Fixa'
    )
    dataRecebimento = models.DateField(verbose_name='Data Recebimento')
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    
    def __str__(self):
        return f"{self.titulo} - {self.valor}"