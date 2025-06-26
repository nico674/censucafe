from django.db import models

# Create your models here.
# models.py
from django.db import models

class EvaluacionCacao(models.Model):
    fecha = models.DateField(auto_now_add=True)

    # ACIDEZ
    acidez = models.FloatField(default=0.0)
    acidez_frutal = models.FloatField(default=0.0)
    acidez_acetica = models.FloatField(default=0.0)
    acidez_lactica = models.FloatField(default=0.0)
    acidez_mineral_butirica = models.FloatField(default=0.0)

    # SABORES NEGATIVOS / DEFECTOS
    amargor = models.FloatField(default=0.0)
    astringencia = models.FloatField(default=0.0)

    # SABORES BASE
    cacao = models.FloatField(default=0.0)
    dulce = models.FloatField(default=0.0)

    # NUEZ
    nuez = models.FloatField(default=0.0)
    parte_interna = models.FloatField(default=0.0)
    piel_nuez = models.FloatField(default=0.0)

    # FRUTAS
    frutas_frescas = models.FloatField(default=0.0)
    fruta_citricos = models.FloatField(default=0.0)
    fruta_bayas = models.FloatField(default=0.0)
    fruta_oscura = models.FloatField(default=0.0)
    fruta_pulpa_amarilla = models.FloatField(default=0.0)
    fruta_tropical = models.FloatField(default=0.0)
    fruta_marron = models.FloatField(default=0.0)
    fruta_seca = models.FloatField(default=0.0)
    fruta_sobre_madura = models.FloatField(default=0.0)

    # VEGETAL
    vegetal_pasto_hierba = models.FloatField(default=0.0)
    vegetal_terroso_hongo_moho = models.FloatField(default=0.0)

    # FLORAL
    floral_flor_azahar = models.FloatField(default=0.0)
    floral_flores = models.FloatField(default=0.0)

    # MADERA
    madera_clara = models.FloatField(default=0.0)
    madera_oscura = models.FloatField(default=0.0)
    madera_resina = models.FloatField(default=0.0)

    # ESPECIAS
    especias = models.FloatField(default=0.0)
    especia_tabaco = models.FloatField(default=0.0)
    especia_umami = models.FloatField(default=0.0)

    # SABORES ATÍPICOS / DEFECTOS
    sucio_empolvado = models.FloatField(default=0.0)
    humedad = models.FloatField(default=0.0)
    mohosa = models.FloatField(default=0.0)
    carnoso_animal_cuero = models.FloatField(default=0.0)
    sobrefermentado_fruta_podrida = models.FloatField(default=0.0)
    podrido_estiercol = models.FloatField(default=0.0)
    humo = models.FloatField(default=0.0)

    # --- Campos automáticos
    acidez_total = models.FloatField(default=0.0)
    defectos_totales = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        self.acidez_total = min(
            self.acidez_frutal +
            self.acidez_acetica +
            self.acidez_lactica +
            self.acidez_mineral_butirica, 10
        )
        self.defectos_totales = min(
            self.sucio_empolvado +
            self.humedad +
            self.mohosa +
            self.carnoso_animal_cuero +
            self.sobrefermentado_fruta_podrida +
            self.podrido_estiercol +
            self.humo +
            self.otro_defecto, 10
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Evaluación {self.fecha}"
