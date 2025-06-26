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

    # Creamos las listas para los gráficos
    fechas = [2]
    acidez = [9]
    amargor = [4]
    dulzor = [9]
    aroma = [2]
    persistencia = [1]

    for e in evaluaciones:
        fechas.append(e.fecha.strftime("%Y-%m-%d"))
        acidez.append(e.acidez)
        amargor.append(e.amargor)
        dulzor.append(e.dulzor)
        aroma.append(e.aroma)
        persistencia.append(e.persistencia)

    contexto = {
        'fechas': json.dumps(fechas),
        'acidez': json.dumps(acidez),
        'amargor': json.dumps(amargor),
        'dulzor': json.dumps(dulzor),
        'aroma': json.dumps(aroma),
        'persistencia': json.dumps(persistencia),
    }

    return render(request, 'admindasboard.html', contexto)

def formcoex(request):
    template1 = loader.get_template('codexform.html')
    return HttpResponse(template1.render())

    
