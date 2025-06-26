from django.db import models

# Create your models here.
# models.py
from django.db import models

class EvaluacionCacao(models.Model):
    fecha = models.DateField(auto_now_add=True)
    acidez = models.FloatField()
    amargor = models.FloatField()
    dulzor = models.FloatField()
    aroma = models.FloatField()
    persistencia = models.FloatField()

    def __str__(self):
        return f"Evaluación del {self.fecha}"
