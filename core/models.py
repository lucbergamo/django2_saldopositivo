from django.db import models

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