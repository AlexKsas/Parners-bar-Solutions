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
from .models import MegustaEventos
from .models import Comentarios
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

@api_view(['GET'])
@csrf_exempt
def obtener_registros_eventos(request):
    registros = eventos.objects.all()
    registros_json = []


    for registro in registros:
        registro_dict = {
            'id': registro.id,
            'nombreEvento': registro.nombreEvento,
            'Latitud': registro.latitud,
            'Longitud': registro.longitud,
            'cover': registro.cover,
            'horarios': registro.horarios,
            'descripcion': registro.descripcion,
            'fechaInicio': registro.fechaInicio,
            'fechaFin': registro.fechaFin,
            'habilitarCanciones': registro.habilitarCanciones,
            "idEstablecimiento": registro.idEstablecimiento
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
    

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_megusta_evento(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_evento = data.get('idEvento')
            id_usuario = data.get('idUsuario')
            
            # Verificar si ya existe un registro con los mismos idEvento e idUsuario
            # Obtener el registro MegustaEventos si existe
            megusta_evento = MegustaEventos.objects.filter(idEvento=id_evento, idUsuario=id_usuario).first()

            if megusta_evento:
                return JsonResponse({'error': 'Ya existe un registro con el mismo idEvento e idUsuario'}, status=400)
            
            nuevo_megusta = MegustaEventos.objects.create(
                idEvento=id_evento,
                idUsuario=id_usuario
            )
            
            return JsonResponse({'mensaje': 'Me gusta creado correctamente'})
        
        except Exception as e:
            print('e')
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'})
    

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_comentario_evento(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_evento = data.get('idEvento')
            id_usuario = data.get('idUsuario')
            comentarioev = data.get('comentario')
            
            nuevo_comentario = Comentarios.objects.create(
                idEvento=id_evento,
                idUsuario=id_usuario,
                comentario=comentarioev
            )
            
            return JsonResponse({'id': nuevo_comentario.id})
        
        except Exception as e:
            print('e')
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'})
    
@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_megusta_evento(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id_evento = data.get('idEvento')
            id_usuario = data.get('idUsuario')

            # Obtener el registro MegustaEventos si existe
            megusta_evento = MegustaEventos.objects.filter(idEvento=id_evento, idUsuario=id_usuario).first()

            if not megusta_evento:
                return JsonResponse({'error': 'No se encuentra un registro con el idEvento e idUsuario proporcionados'}, status=400)

            # Eliminar el registro
            megusta_evento.delete()

            return JsonResponse({'mensaje': 'Me gusta evento eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones DELETE'})
    
@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_comentario_evento(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id_comentario = data.get('id')

            # Obtener el registro comentario si existe
            comentario_evento = Comentarios.objects.filter(id=id_comentario).first()

            if not comentario_evento:
                return JsonResponse({'error': 'No se encuentra ningun comentario con ese id'}, status=400)

            # Eliminar el registro
            comentario_evento.delete()

            return JsonResponse({'mensaje': 'comentario evento eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones DELETE'})
    
@csrf_exempt
@api_view(['POST'])
def obtener_megusta_evento(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_evento = data.get('idEvento')

            # Obtener todos los "Me gusta" del evento
            megusta_eventos = MegustaEventos.objects.filter(idEvento=id_evento)
            
            registros_json = []

            for registro in megusta_eventos:
                registro_dict = {
                    'id': registro.id,
                    'idEvento': registro.idEvento,
                    'idUsuario': registro.idUsuario,
                }
                registros_json.append(registro_dict)

            return JsonResponse({'registros': registros_json})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'})
    
@csrf_exempt
@api_view(['POST'])
def obtener_comentarios_evento(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_evento = data.get('idEvento')

            # Obtener todos los "comentarios" del evento
            comentario_eventos = Comentarios.objects.filter(idEvento=id_evento)
            
            registros_json = []

            for registro in comentario_eventos:
                registro_dict = {
                    'id': registro.id,
                    'idEvento': registro.idEvento,
                    'idUsuario': registro.idUsuario,
                    'comentario': registro.comentario,
                }
                registros_json.append(registro_dict)

            return JsonResponse({'registros': registros_json})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'})
