from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login
#from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
import json
from .models import EvaluacionCacao


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

   

def formcoex(request):
    template1 = loader.get_template('codexform.html')
    return HttpResponse(template1.render())

    
