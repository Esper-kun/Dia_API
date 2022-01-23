from django.db import models

# Create your models here.

class Dia(models.Model):
    FRACA =    'FR'
    MODERADA = 'MD'
    FORTE =    'FT'
    INTENSA =  'IT'

    ESCOLHAS = [
        (FRACA, 'Fraca'),
        (MODERADA, 'Moderada'),
        (FORTE, 'Forte'),
        (INTENSA, 'Intensa')
    ]

    id_dia = models.DateField(primary_key=True)
    tipo_fluxo = models.CharField(max_length=2, choices=ESCOLHAS, default=FRACA)
    tipo_dor = models.CharField(max_length=2, choices=ESCOLHAS, default=FRACA)
    tipo_TPM = models.CharField(max_length=2, choices=ESCOLHAS, default=FRACA)
