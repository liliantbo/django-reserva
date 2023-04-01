from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def getInfoCanchaById(request, id_cancha):
    cancha = Cancha.objects.get(id=id_cancha)
    result_layout = f"<h3>Cancha: {cancha.nombre}, Descripción: {cancha.descipcion}</h3>"

    return HtttpResponse(result_layout)