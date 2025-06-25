from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login
#from django.contrib import messages
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def admindasboard(request):
    template = loader.get_template('admindasboard.html')
    return HttpResponse(template.render())

def formcoex(request):
    template1 = loader.get_template('codexform.html')
    return HttpResponse(template1.render())

    
