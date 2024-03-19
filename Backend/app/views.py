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
import json
from django.http import JsonResponse
from pymongo import MongoClient
from django.conf import settings
from bson.json_util import dumps

# Create your views here.
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def consulta_discotecas_cercanas(request):
    print('@1')
    # Establecer conexión con la base de datos MongoDB
    client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
    db = client[settings.DATABASES['default']['NAME']]
    print('@2')
    # Definir el query que deseas ejecutar
    query = [
        {
            '$geoNear': {
                'near': [-74.0859828, 4.6414189],
                'distanceField': "distance",
                'maxDistance': 2000,
                'distanceMultiplier': 6371,
                'spherical': True
            }
        }
    ]
    print('@3')
    # Ejecutar el query en la colección "lugares"
    resultados = db['Discotecas'].aggregate(query)
    res = json.loads(dumps(resultados))
    print('@4')
    print('@@@',res)
    # Procesar los resultados
    lugares = []
    for lugar in resultados:
        lugares.append({
            'name': lugar['Nombre'],
            'location': lugar['location'],
            'nit': lugar['Nit']
        })
    print('@5')
    print('@@',lugares)
    # Cerrar la conexión con la base de datos MongoDB
    client.close()

    # Devolver los resultados como una respuesta JSON
    return JsonResponse({'resultados': lugares})



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


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_registro_establecimientos(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            Rid = data.get('id')
            RNombreEstablecimiento = data.get('NombreEstablecimiento')
            RLatitud = data.get('Latitud')
            RLongitud = data.get('Longitud')
            RidHorario = data.get('idHorario')
            
            # Crear un nuevo registro de establecimiento
            nuevo_registro = Establecimientos.objects.create(
                id=Rid,
                NombreEstablecimiento=RNombreEstablecimiento,
                Latitud=RLatitud,
                Longitud=RLongitud,
                idHorario=RidHorario

            )
            
            return JsonResponse({'mensaje': 'Registro creado correctamente'})
        
        except Exception as e:
            return JsonResponse({'error': str(e)})

    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'})
