from django.shortcuts import render
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Establecimientos

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def obtener_registros_establecimientos(request):
    registros = Establecimientos.objects.all()
    registros_json = []

    for registro in registros:
        registro_dict = {
            'id': registro.id,
            'NombreEstablecimiento': registro.NombreEstablecimiento,
            'Latitud': registro.Latitud,
            'Longitud': registro.Longitud,
            'idHorario': registro.idHorario,
        }
        registros_json.append(registro_dict)

    return JsonResponse({'registros': registros_json})
