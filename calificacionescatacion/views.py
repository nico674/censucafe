from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login
#from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
import json
from .models import EvaluacionCacao
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def admindasboard(request):
        # Consultamos todas las evaluaciones ordenadas por fecha
    evaluaciones = EvaluacionCacao.objects.order_by('fecha')

    # ejemplo con varios atributos
    fechas = [1]
    acidez = [2]
    acidez_frutal = [4]
    amargor = [4]
    fruta_tropical = [5]
    humedad = [5]
    humo = [3]

    for e in evaluaciones:
        fechas.append(e.fecha.strftime("%Y-%m-%d"))
        acidez.append(e.acidez)
        acidez_frutal.append(e.acidez_frutal)
        amargor.append(e.amargor)
        fruta_tropical.append(e.fruta_tropical)
        humedad.append(e.humedad)
        humo.append(e.humo)

    contexto = {
        'fechas': json.dumps(fechas),
        'acidez': json.dumps(acidez),
        'acidez_frutal': json.dumps(acidez_frutal),
        'amargor': json.dumps(amargor),
        'fruta_tropical': json.dumps(fruta_tropical),
        'humedad': json.dumps(humedad),
        'humo': json.dumps(humo),
    }

    return render(request, 'admindasboard.html', contexto)

   

@csrf_protect
def formcoex(request):
    if request.method == 'POST':
        muestra = request.POST.get('muestra')
        catador = request.POST.get('catador')
        fecha = request.POST.get('fecha')

        evaluacion = EvaluacionCacao(
            muestra=muestra,
            catador=catador,
            fecha=fecha,

            # ACIDEZ
            acidez_frutal_intensidad=request.POST.get('acidez_frutal_intensidad', 0),
            acidez_frutal_descripcion=request.POST.get('acidez_frutal_descripcion', ''),
            acidez_frutal_calidad=request.POST.get('acidez_frutal_calidad', 0),
            acidez_frutal_score=request.POST.get('acidez_frutal_score', 0),

            acidez_acetica_intensidad=request.POST.get('acidez_acetica_intensidad', 0),
            acidez_acetica_descripcion=request.POST.get('acidez_acetica_descripcion', ''),
            acidez_acetica_calidad=request.POST.get('acidez_acetica_calidad', 0),
            acidez_acetica_score=request.POST.get('acidez_acetica_score', 0),

            acidez_lactica_intensidad=request.POST.get('acidez_lactica_intensidad', 0),
            acidez_lactica_descripcion=request.POST.get('aroma_desc', ''),
            acidez_lactica_calidad=request.POST.get('acidez_qual', 0),
            acidez_lactica_score=request.POST.get('acidez_score', 0),

            acidez_mineral_intensidad=request.POST.get('acidez_mineral_intensidad', 0),
            acidez_mineral_descripcion=request.POST.get('acidez_mineral_descripcion', ''),
            acidez_mineral_calidad=request.POST.get('acidez_mineral_calidad', 0),
            acidez_mineral_score=request.POST.get('acidez_mineral_score', 0),

            # AMARGOR
            amargor_intensidad=request.POST.get('amargor_intensidad', 0),
            amargor_descripcion=request.POST.get('amargor_descripcion', ''),
            amargor_calidad=request.POST.get('amargor_calidad', 0),
            amargor_score=request.POST.get('amargor_score', 0),

            # ASTRINGENCIA
            astringencia_intensidad=request.POST.get('astringencia_intensidad', 0),
            astringencia_descripcion=request.POST.get('astringencia_descripcion', ''),
            astringencia_calidad=request.POST.get('astringencia_calidad', 0),
            astringencia_score=request.POST.get('astrigencia_score', 0),

            # CACAO
            cacao_intensidad=request.POST.get('cacao_intensidad', 0),
            cacao_descripcion=request.POST.get('cacao_descripcion', ''),
            cacao_calidad=request.POST.get('cacao_calidad', 0),
            cacao_score=request.POST.get('cacao_score', 0),

            # DULCE
            dulce_intensidad=request.POST.get('dulce_int', 0),
            dulce_descripcion=request.POST.get('dulce_desc', ''),
            dulce_calidad=request.POST.get('dulce_calidad', 0),
            dulce_score=request.POST.get('dulce_score', 0),

            nuez_intensidad=request.POST.get('nuez_int', 0),
            nuez_descripcion=request.POST.get('nuez_desc', ''),
            nuez_calidad=request.POST.get('nuez_calidad', 0),
            nuez_score=request.POST.get('nuez_score', 0),

            

            # Otros atributos siguen aquí (nuez, frutas, floral, madera, especias, sabores atípicos…)
            # Sigue el mismo patrón: 
            # atributo_intensidad, atributo_descripcion, atributo_calidad, atributo_score

            # COMENTARIOS Y PUNTAJE FINAL
            comentarios=request.POST.get('comentarios', ''),
            catador_score=request.POST.get('catador_score', 0),
            puntaje_final=request.POST.get('puntaje_final', 0)
        )
        evaluacion.save()
        return redirect('dashboard')

    return render(request, 'codexform.html')

