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
from .models import eventos
import json
from django.http import JsonResponse
from pymongo import MongoClient
from django.conf import settings
from bson.json_util import dumps

# Create your views here.


"""
@api_view(['POST'])
@permission_classes([IsAuthenticated])"""
@csrf_exempt
def consulta_discotecas_cercanas(request):
    print('@1')
    data = json.loads(request.body)
    # Obtener las fechas inicial y final del cuerpo JSON
    latitud = data.get('latitud')
    longitud = data.get('longitud')
    distancia_maxima = data.get('distancia_maxima')
    #latitud =   -74.0759 #request.GET.get('latitud')
    #longitud =  4.6514  #request.GET.get('longitud')
    #distancia_maxima = 295 #request.GET.get('distancia_maxima')
    # Establecer conexión con la base de datos MongoDB
    client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
    db = client[settings.DATABASES['default']['NAME']]
    print('@2')
    """
    query = [
        {
            '$geoNear': {
                'near': [float(longitud), float(latitud)],
                'distanceField': "distancia",
                'maxDistance': float(distancia_maxima),
                'distanceMultiplier': 6371,
                'spherical': True
            }
        }
    ]
    """
    query = [
        {
            '$geoNear':{
                'near':{
                    'type':"Point",
                    'coordinates': [float(longitud), float(latitud)]
                },
                'distanceField': "distancia",
                'maxDistance': float(distancia_maxima)
                
            }
        }
    ]

    print('query',query)

    print('@3')
    # Ejecutar el query en la colección "lugares"
    resultados = db['Discotecas'].aggregate(query)
    print('@@@4')
    print('-----',resultados)
    res = json.loads(dumps(resultados))
    print('@4')
    print('@@@',res)
    # Procesar los resultados
    
    return JsonResponse({'resultados': res})



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
    

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_evento(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latitud = data.get('latitud')
            longitud = data.get('longitud')
            nombreEvento = data.get('nombreEvento')
            cover = data.get('cover')
            horarios = data.get('horarios')
            descripcion = data.get('descripcion')
            fechaInicio = data.get('fechaInicio')
            fechaFin = data.get('fechaFin')
            habilitarCanciones = data.get('habilitarCanciones')
            idEstablecimiento = data.get('idEstablecimiento')
            
            # Crear un nuevo evento
            nuevo_evento = eventos.objects.create(
                latitud=latitud,
                longitud=longitud,
                nombreEvento=nombreEvento,
                cover=cover,
                horarios=horarios,
                descripcion=descripcion,
                fechaInicio=fechaInicio,
                fechaFin=fechaFin,
                habilitarCanciones=habilitarCanciones,
                idEstablecimiento=idEstablecimiento
            )
            
            # Retornar el ID del evento creado
            return JsonResponse({'id': nuevo_evento.id})
        
        except Exception as e:
            return JsonResponse({'error': str(e)})

    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'})
