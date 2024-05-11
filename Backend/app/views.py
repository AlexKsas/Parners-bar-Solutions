from django.shortcuts import render
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import eventos
from .models import MegustaEventos
from .models import MegustaEstablecimiento
from .models import Comentarios
from .models import Productos
from .models import Asistencia
from .models import ListadoCanciones
import json
from django.http import JsonResponse
from pymongo import MongoClient
from rest_framework_simplejwt.tokens import Token
from django.conf import settings
from bson.json_util import dumps
import uuid
from django.contrib.auth import get_user_model
import jwt


# Create your views here.


#BD:

client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
db = client[settings.DATABASES['default']['NAME']]



'''------------------------------@discotecas-----------------------------------'''
'''------------------------------@discotecas-----------------------------------'''
'''------------------------------@discotecas-----------------------------------'''
'''------------------------------@discotecas-----------------------------------'''
'''------------------------------@discotecas-----------------------------------'''
@csrf_exempt
def obtener_registros_establecimientos(request):
    todas_las_discotecas = db['Discotecas'].find({})
    res = json.loads(dumps(todas_las_discotecas))
    
    # Procesar los resultados
    registros_validos = []
    for disco in res:
        disco['numeroLikes'] = obtener_numero_likes_establecimiento(disco['id'])
        registros_validos.append(disco)
    
    return JsonResponse({'resultados': registros_validos})

@csrf_exempt
def obtener_discotecaCel(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_discoteca = data.get('id_discoteca')
            # Verificar si se proporcionó un ID de discoteca en el cuerpo de la petición
            if id_discoteca is None:
                return JsonResponse({'error': 'Se requiere proporcionar un ID de discoteca en el cuerpo de la petición'}, status=400)
            
            # Buscar la discoteca por su ID en la base de datos
            discoteca = db['Discotecas'].find_one({'id': id_discoteca})
            
            if discoteca:
                discoteca['numeroLikes'] = obtener_numero_likes_establecimiento(discoteca['id'])
                res = json.loads(dumps(discoteca))
                # Procesar los resultados
                return JsonResponse({'resultados': res})
                
            else:
                # Si no se encontró la discoteca, devolver un error
                return JsonResponse({'error': 'No se encontró ninguna discoteca con el ID proporcionado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)
    


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_discotecaPc(request):
    if request.method == 'GET':
        try:
            
            authorization_header = request.headers.get('Authorization')
            _, token = authorization_header.split(None, 1)
            # Eliminar el prefijo 'Bearer ' si está presente en el token
            token = token.replace('Bearer ', '')
            # Ahora el token contiene solo el token sin el prefijo 'Bearer'
            id_usuario = obtenerIdUser(token)
            id_discoteca = obtener_establecimiento_de_usuario_por_id(id_usuario)
            
            # Verificar si se proporcionó un ID de discoteca en el cuerpo de la petición
            if id_discoteca is None:
                return JsonResponse({'error': 'El usuario no tiene un establecimeinto relacionado'}, status=400)
            
            # Buscar la discoteca por su ID en la base de datos
            discoteca = db['Discotecas'].find_one({'id': id_discoteca})
            
            if discoteca:
                discoteca['numeroLikes'] = obtener_numero_likes_establecimiento(discoteca['id'])
                discoteca['email'] = obtener_email_establecimiento(discoteca['id'])
                res = json.loads(dumps(discoteca))
                # Procesar los resultados
                return JsonResponse({'resultados': res})
            else:
                # Si no se encontró la discoteca, devolver un error
                return JsonResponse({'error': 'No se encontró ninguna discoteca para ese usuario'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones GET'}, status=400)




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
    
    print('@2')
    
    query = [
        {
            '$geoNear':{
                'near':{
                    'type':"Point",
                    'coordinates': [float(latitud), float(longitud)]
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
    # Procesar los resultados
    registros_validos = []
    for disco in res:
        disco['numeroLikes'] = obtener_numero_likes_establecimiento(disco['id'])
        registros_validos.append(disco)
    
    print('@4')
    print('@@@',res)
    # Procesar los resultados
    return JsonResponse({'resultados': registros_validos})
    



@csrf_exempt
def crear_discoteca(request):
    if request.method == 'POST':
        try:
            # Load JSON data from request body
            data = json.loads(request.body)

            #datos usuario 
            User = get_user_model()
            username = data.get('correoUsuario')  # Nombre de usuario desde el formulario
            password = data.get('contrasenaUsuario')  # Contraseña desde el formulario
            cedula = data.get('numeroIdentificacionUsuario')
            celular = data.get('celularUsuario')
            tipoIdentificacion = data.get('tipoIdentificacionUsuario')
            first_name = data.get('nombreUsuario')  # Nombre desde el formulario
            last_name = data.get('apellidoUsuario')

            # datos para establecimiento
            id = str(uuid.uuid4())
            Nombre = data.get('nombreEstablecimiento')
            latitud = float(data.get('latitud'))
            longitud = float(data.get('longitud'))
            Horario = data.get('horario')
            Imagen = data.get('imagen')
            Telefono = data.get('telefono')
            Descripcion = data.get('descripcion')

            # Validate required fields
            if not id or not Nombre or not latitud or not longitud or not Horario or not Imagen or not Telefono or not username or not password or not cedula or not celular or not tipoIdentificacion or not first_name or not last_name:
                return JsonResponse({'error': 'faltan campos requeridos'}, status=400)
            
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.cedula = cedula
                user.celular = celular
                user.tipoIdentificacion = tipoIdentificacion
                user.idEstablecimiento = id
                user.save()
                # Create discoteca document
                discoteca_document = {
                    'id': id,
                    'Nombre': Nombre,
                    'location': {
                        'type': 'Point',
                        'coordinates': [latitud, longitud]
                    },
                    'Horario': Horario,
                    'Imagen': Imagen,
                    'Telefono': Telefono,
                    'Descripcion': Descripcion,
                    'Estado':0
                }

                # Insert discoteca document into MongoDB
                db['Discotecas'].insert_one(discoteca_document)

                # Return success response
                return JsonResponse({'message': 'Establecimiento creada con éxito', 'id': id})
            else:
                return JsonResponse({'error': 'El usuario ya existe'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'},status=400)


'''------------------------------@usuarios-----------------------------------'''
'''------------------------------@usuarios-----------------------------------'''
'''------------------------------@usuarios-----------------------------------'''
'''------------------------------@usuarios-----------------------------------'''
'''------------------------------@usuarios-----------------------------------'''

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def consultar_usuario(request):
    if request.method == 'GET':
        try:
            User = get_user_model()
            authorization_header = request.headers.get('Authorization')
            _, token = authorization_header.split(None, 1)
            # Eliminar el prefijo 'Bearer ' si está presente en el token
            token = token.replace('Bearer ', '')
            # Ahora el token contiene solo el token sin el prefijo 'Bearer'
            id_usuario = obtenerIdUser(token)
            # Crear el nuevo usuario
            user= User.objects.get(id=id_usuario)
            user_info = {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'cedula': user.cedula,
                'celular': user.celular,
                'tipoIdentificacion': user.tipoIdentificacion,
                'direccion': user.direccion,
                'imagen': user.imagen,
                'fechaNacimiento': user.fechaNacimiento,
                'edad': user.edad,
                'genero': user.genero
            }
            return JsonResponse(user_info)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'El método de solicitud debe ser GET'}, status=400)




@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            User = get_user_model()
            username = data.get('correo')  # Nombre de usuario desde el formulario
            password = data.get('contrasena')  # Contraseña desde el formulario
            cedula = data.get('numeroIdentificacion')
            celular = data.get('celular')
            tipoIdentificacion = data.get('tipoIdentificacion')
            first_name = data.get('nombre')  # Nombre desde el formulario
            last_name = data.get('apellido')  # Apellido desde el formulario
            direccion = data.get('direccion')
            imagen = data.get('imagen')
            fechaNacimiento = data.get('fechaNacimiento')
            edad = data.get('edad')
            genero = data.get('genero')
        

            # Verificar que los campos requeridos no estén vacíos
            if not all([username, password, first_name, last_name,cedula,celular,direccion,fechaNacimiento,edad,genero,tipoIdentificacion]):
                return JsonResponse({'error': 'Por favor, complete todos los campos.'}, status=400)

            # Crear el nuevo usuario
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.cedula = cedula
                user.celular = celular
                user.tipoIdentificacion = tipoIdentificacion
                user.direccion = direccion
                user.imagen = imagen
                user.fechaNacimiento = fechaNacimiento
                user.edad = edad
                user.genero = genero

                user.save()
                return JsonResponse({'mensaje': 'Usuario creado correctamente'})
            else:
                return JsonResponse({'error': 'El usuario ya existe'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'El método de solicitud debe ser POST'}, status=400)



@csrf_exempt
def obtener_evento(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_evento = data.get('id_evento')
            # Verificar si se proporcionó un ID de discoteca en el cuerpo de la petición
            if id_evento is None:
                return JsonResponse({'error': 'Se requiere proporcionar un ID de evento en el cuerpo de la petición'}, status=400)
            
            # Buscar la discoteca por su ID en la base de datos
            evento = eventos.objects.filter(id=id_evento).first()
            # Buscar la discoteca por su ID en la base de datos
            discoteca = db['Discotecas'].find_one({'id': evento.idEstablecimiento})
            
            if evento:
                res = {
                    "id":evento.id,
                    "latitud":evento.latitud,
                    "longitud":evento.longitud,
                    "nombreEvento":evento.nombreEvento,
                    "cover":evento.cover,
                    "horarios":evento.horarios,
                    "descripcion":evento.descripcion,
                    "fechaInicio":evento.fechaInicio,
                    "fechaFin":evento.fechaFin,
                    "habilitarCanciones":evento.habilitarCanciones,
                    "idEstablecimiento":evento.idEstablecimiento,
                    "imagen":evento.imagen,
                    "numeroLikes":obtener_numero_likes_evento(evento.id),
                    "nombreEstablecimiento": discoteca['Nombre'] if discoteca else '',
                    "imagenEstablecimiento": discoteca['Imagen'] if discoteca else ''

                }
                return JsonResponse({'info': res})
                
            else:
                # Si no se encontró la discoteca, devolver un error
                return JsonResponse({'error': 'No se encontró ningun evento con el ID proporcionado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)


@api_view(['GET'])
@csrf_exempt
def obtener_registros_eventos(request):
    registros = eventos.objects.all()
    registros_json = []

    

    for registro in registros:
        # Buscar la discoteca por su ID en la base de datos
        discoteca = db['Discotecas'].find_one({'id': registro.idEstablecimiento})
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
            "idEstablecimiento": registro.idEstablecimiento,
            "imagen":registro.imagen,
            "numeroLikes":obtener_numero_likes_evento(registro.id),
            "nombreEstablecimiento": discoteca['Nombre'] if discoteca else '',
            "imagenEstablecimiento": discoteca['Imagen'] if discoteca else ''
        }
        registros_json.append(registro_dict)

    return JsonResponse({'registros': registros_json})

@api_view(['POST'])
@csrf_exempt
def obtener_registros_eventos_por_establecimiento(request):
    data = json.loads(request.body)
    registros = eventos.objects.filter(idEstablecimiento=data.get('idEstablecimiento'))
    registros_json = []


    for registro in registros:
        # Buscar la discoteca por su ID en la base de datos
        discoteca = db['Discotecas'].find_one({'id': registro.idEstablecimiento})
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
            "idEstablecimiento": registro.idEstablecimiento,
            "imagen":registro.imagen,
            "numeroLikes":obtener_numero_likes_evento(registro.id),
            "nombreEstablecimiento": discoteca['Nombre'] if discoteca else '',
            "imagenEstablecimiento": discoteca['Imagen'] if discoteca else ''
            
        }
        registros_json.append(registro_dict)

    return JsonResponse({'registros': registros_json})



@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_evento(request):
    if request.method == 'POST':
        try:
            authorization_header = request.headers.get('Authorization')
            # Separar el tipo de esquema de autenticación y el token
            _, token = authorization_header.split(None, 1)
            # Eliminar el prefijo 'Bearer ' si está presente en el token
            token = token.replace('Bearer ', '')
    
            id_usuario = obtenerIdUser(token)
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
            idEstablecimiento = obtener_establecimiento_de_usuario_por_id(id_usuario)
            if(idEstablecimiento):
                print('encontro establecimiento')
            else:
                return JsonResponse({'error': 'No se encontro establecimiento para ese usuario'},status=400)
                
            imagenint = data.get('imagen')
            
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
                idEstablecimiento=idEstablecimiento,
                imagen=imagenint
            )
            
            # Retornar el ID del evento creado
            return JsonResponse({'id': nuevo_evento.id})
        
        except Exception as e:
            return JsonResponse({'error': str(e)})

    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)
    

@csrf_exempt
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def actualizar_evento(request):
    if request.method == 'PUT':
        try:
            authorization_header = request.headers.get('Authorization')
            # Separar el tipo de esquema de autenticación y el token
            _, token = authorization_header.split(None, 1)
            # Eliminar el prefijo 'Bearer ' si está presente en el token
            token = token.replace('Bearer ', '')
    
            id_usuario = obtenerIdUser(token)
            idEstablecimiento = obtener_establecimiento_de_usuario_por_id(id_usuario)
            id_evento = json.loads(request.body).get('id')
            evento_a_actualizar = eventos.objects.get(id=id_evento)

            if evento_a_actualizar.idEstablecimiento != idEstablecimiento:
                return JsonResponse({'error': 'Usuario no esta relacionado al establecimiento del evento'}, status=400)


            data = json.loads(request.body)
            for campo, valor in data.items():
                if campo in ['latitud', 'longitud', 'nombreEvento', 'cover', 'horarios', 'descripcion', 'fechaInicio', 'fechaFin', 'habilitarCanciones', 'imagen']:
                    setattr(evento_a_actualizar, campo, valor)

            evento_a_actualizar.save()  # Guardar los cambios en el evento actualizado

            return JsonResponse({'mensaje': 'Evento actualizado correctamente'})
        except eventos.DoesNotExist:
            return JsonResponse({'error': 'No se encontró evento relacionado al usuario que envia token'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones PUT'}, status=400)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_megusta_evento(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            authorization_header = request.headers.get('Authorization')
            # Separar el tipo de esquema de autenticación y el token
            _, token = authorization_header.split(None, 1)
            # Eliminar el prefijo 'Bearer ' si está presente en el token
            token = token.replace('Bearer ', '')
    
            id_usuario = obtenerIdUser(token)
            id_evento = data.get('idEvento')
            
            
            # Verificar si ya existe un registro con los mismos idEvento e idUsuario
            # Obtener el registro MegustaEventos si existe
            megusta_evento = MegustaEventos.objects.filter(idEvento=id_evento, idUsuario=id_usuario).first()

            if megusta_evento:
                # Si ya existe, eliminar el registro
                megusta_evento.delete()
                return JsonResponse({'mensaje': 'Se elimino like'})
            else:
                # Si no existe, crear un nuevo registro
                nuevo_megusta = MegustaEventos.objects.create(
                    idEvento=id_evento,
                    idUsuario=id_usuario
                )
                return JsonResponse({'mensaje': 'Like creado correctamente'})
        
        except Exception as e:
            print('e')
            return JsonResponse({'error': str(e)},status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'},status=400)
    
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_megusta_establecimiento(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            authorization_header = request.headers.get('Authorization')
            # Separar el tipo de esquema de autenticación y el token
            _, token = authorization_header.split(None, 1)
            # Eliminar el prefijo 'Bearer ' si está presente en el token
            token = token.replace('Bearer ', '')
    
            id_usuario = obtenerIdUser(token)
            id_establecimiento = data.get('idEstablecimiento')
            
            
            # Verificar si ya existe un registro con los mismos idEvento e idUsuario
            # Obtener el registro MegustaEventos si existe
            megusta_establecimiento = MegustaEstablecimiento.objects.filter(idEstablecimiento=id_establecimiento, idUsuario=id_usuario).first()

            if megusta_establecimiento:
                # Si ya existe, eliminar el registro
                megusta_establecimiento.delete()
                return JsonResponse({'mensaje': 'Se elimino like'})
            else:
                # Si no existe, crear un nuevo registro
                nuevo_megusta = MegustaEstablecimiento.objects.create(
                    idEstablecimiento=id_establecimiento,
                    idUsuario=id_usuario
                )
                return JsonResponse({'mensaje': 'Like creado correctamente'})
        
        except Exception as e:
            print('e')
            return JsonResponse({'error': str(e)},status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'},status=400)
    

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_comentario_evento(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            authorization_header = request.headers.get('Authorization')
            if authorization_header:
                # Separar el tipo de esquema de autenticación y el token
                _, token = authorization_header.split(None, 1)
                # Eliminar el prefijo 'Bearer ' si está presente en el token
                token = token.replace('Bearer ', '')
                # Ahora el token contiene solo el token sin el prefijo 'Bearer'
                print('Token:', token)
                id_evento = data.get('idEvento')
                id_usuario = obtenerIdUser(token)
                comentarioev = data.get('comentario')
            
                nuevo_comentario = Comentarios.objects.create(
                    idEvento=id_evento,
                    idUsuario=id_usuario,
                    comentario=comentarioev
                )
            
            return JsonResponse({'id': nuevo_comentario.id})
        
        except Exception as e:
            print('e')
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)
    
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
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones DELETE'}, status=400)
    
@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_comentario_evento(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id_comentario = data.get('id')
            authorization_header = request.headers.get('Authorization')
            # Separar el tipo de esquema de autenticación y el token
            _, token = authorization_header.split(None, 1)
            # Eliminar el prefijo 'Bearer ' si está presente en el token
            token = token.replace('Bearer ', '')
    
            id_usuario = obtenerIdUser(token)

            # Obtener el registro comentario si existe
            comentario_evento = Comentarios.objects.filter(id=id_comentario).first()

            if not comentario_evento:
                return JsonResponse({'error': 'No se encuentra ningun comentario con ese id'}, status=400)

            # Eliminar el registro
            if comentario_evento.idUsuario != str(id_usuario):
                return JsonResponse({'error': 'Usuario idUsuario no corresponde al usuario de este comentario'}, status=400)

            comentario_evento.delete()

            return JsonResponse({'mensaje': 'comentario evento eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones DELETE'}, status=400)
    
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
                    'nombreUsuario': obtener_nombre_de_usuario_por_id(registro.idUsuario),
                    'idUsuario': registro.idUsuario,
                }
                registros_json.append(registro_dict)

            return JsonResponse({'registros': registros_json})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)
    
@csrf_exempt
@api_view(['POST'])
def obtener_megusta_establecimiento(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_establecimiento = data.get('idEstablecimiento')

            # Obtener todos los "Me gusta" del evento
            megusta_establecimiento = MegustaEstablecimiento.objects.filter(idEstablecimiento=id_establecimiento)
            
            registros_json = []

            for registro in megusta_establecimiento:
                registro_dict = {
                    'id': registro.id,
                    'idEstablecimiento': registro.idEstablecimiento,
                    'nombreUsuario': obtener_nombre_de_usuario_por_id(registro.idUsuario),
                    'idUsuario': registro.idUsuario,
                }
                registros_json.append(registro_dict)

            return JsonResponse({'registros': registros_json})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)
    
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
                    'nombreUsuario': obtener_nombre_de_usuario_por_id(registro.idUsuario),
                    'comentario': registro.comentario,
                }
                registros_json.append(registro_dict)

            return JsonResponse({'registros': registros_json})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)
    

'''------------------------------@productos-----------------------------------'''
'''------------------------------@productos-----------------------------------'''
'''------------------------------@productos-----------------------------------'''
'''------------------------------@productos-----------------------------------'''
'''------------------------------@productos-----------------------------------'''

    
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_producto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            authorization_header = request.headers.get('Authorization')
            if authorization_header:
                # Separar el tipo de esquema de autenticación y el token
                _, token = authorization_header.split(None, 1)
                # Eliminar el prefijo 'Bearer ' si está presente en el token
                token = token.replace('Bearer ', '')
                # Ahora el token contiene solo el token sin el prefijo 'Bearer'
                id_usuario = obtenerIdUser(token)
                id_dicoteca = obtener_establecimiento_de_usuario_por_id(id_usuario)
                nombre_producto = data.get('nombre')
                precio_producto = data.get('precio')
                categoria_producto = data.get('categoria')
                urlImagen_producto = data.get('imagen')
            
                nuevo_producto = Productos.objects.create(
                    idEstablecimiento = id_dicoteca,
                    nombre = nombre_producto,
                    precio = precio_producto,
                    categoria = categoria_producto,
                    urlImagen = urlImagen_producto
                )
            
            return JsonResponse({'id': nuevo_producto.id})
        
        except Exception as e:
            print('e')
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)
    





@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_producto(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            authorization_header = request.headers.get('Authorization')
            if authorization_header:
                # Separar el tipo de esquema de autenticación y el token
                _, token = authorization_header.split(None, 1)
                # Eliminar el prefijo 'Bearer ' si está presente en el token
                token = token.replace('Bearer ', '')
                # Ahora el token contiene solo el token sin el prefijo 'Bearer'
                id_usuario = obtenerIdUser(token)
                id_dicoteca = obtener_establecimiento_de_usuario_por_id(id_usuario)
                
                id_producto = data.get('id')
                
                # Verificar si el producto pertenece al establecimiento del usuario
                producto = Productos.objects.get(id=id_producto)
                if producto.idEstablecimiento == id_dicoteca:
                    producto.delete()
                    return JsonResponse({'mensaje': 'Producto eliminado correctamente'})
                else:
                    return JsonResponse({'error': 'El usuario no puede eliminar este producto, no pertenece al establecimiento'}, status=400)
            else:
                return JsonResponse({'error': 'Se requiere un token de autenticación'}, status=400)
        except Productos.DoesNotExist:
            return JsonResponse({'error': 'El producto no existe'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones DELETE'}, status=400)
    


@csrf_exempt
def obtener_productosCel(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_discoteca = data.get('id_discoteca')
            # Verificar si se proporcionó un ID de discoteca en el cuerpo de la petición
            if id_discoteca is None:
                return JsonResponse({'error': 'Se requiere proporcionar un ID de discoteca en el cuerpo de la petición'}, status=400)
            
            # Buscar la discoteca por su ID en la base de datos
            registros = Productos.objects.filter(idEstablecimiento = id_discoteca)
            
            registros_json = []

            for registro in registros:
                registro_dict = {
                    'id': registro.id,
                    'nombre': registro.nombre,
                    'precio':registro.precio,
                    'categoria': registro.categoria,
                    'imagen': registro.urlImagen
                }
                registros_json.append(registro_dict)

            return JsonResponse({'registros': registros_json})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)



@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_productosPc(request):
    if request.method == 'GET':
        try:
            authorization_header = request.headers.get('Authorization')
            _, token = authorization_header.split(None, 1)
            # Eliminar el prefijo 'Bearer ' si está presente en el token
            token = token.replace('Bearer ', '')
            # Ahora el token contiene solo el token sin el prefijo 'Bearer'
            id_usuario = obtenerIdUser(token)
            id_discoteca = obtener_establecimiento_de_usuario_por_id(id_usuario)
            
            # Verificar si se proporcionó un ID de discoteca en el cuerpo de la petición
            if id_discoteca is None:
                return JsonResponse({'error': 'El usuario no tiene un establecimeinto relacionado'}, status=400)
            
            # Buscar la discoteca por su ID en la base de datos
            registros = Productos.objects.filter(idEstablecimiento = id_discoteca)
            
            registros_json = []

            for registro in registros:
                registro_dict = {
                    'id': registro.id,
                    'nombre': registro.nombre,
                    'precio':registro.precio,
                    'categoria': registro.categoria,
                    'imagen': registro.urlImagen
                }
                registros_json.append(registro_dict)

            return JsonResponse({'registros': registros_json})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)





'''-----------------------------------asistencia-------------------------------------'''
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_asistencia(request):
    if request.method == 'POST':
        try:
            authorization_header = request.headers.get('Authorization')
            # Separar el tipo de esquema de autenticación y el token
            _, token = authorization_header.split(None, 1)
            # Eliminar el prefijo 'Bearer ' si está presente en el token
            token = token.replace('Bearer ', '')
    
            id_usuario = obtenerIdUser(token)
            data = json.loads(request.body)
            idevent = data.get('idEvento')
            fechaingres = data.get('fechaIngreso')
            
            # Crear un nuevo evento
            nueva_asistencia = Asistencia.objects.create(
                idUsuario=id_usuario,
                idEvento=idevent,
                fechaIngreso=fechaingres
            )
            
            # Retornar el ID del evento creado
            return JsonResponse({'id': nueva_asistencia.id})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)
    
@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_asistencia(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            authorization_header = request.headers.get('Authorization')
            if authorization_header:
                # Separar el tipo de esquema de autenticación y el token
                _, token = authorization_header.split(None, 1)
                # Eliminar el prefijo 'Bearer ' si está presente en el token
                token = token.replace('Bearer ', '')
                # Ahora el token contiene solo el token sin el prefijo 'Bearer'
                id_usuario = obtenerIdUser(token)
                
                id_asistencia = data.get('id')
                
                # Verificar si el producto pertenece al establecimiento del usuario
                registro = Asistencia.objects.get(id=id_asistencia)

                
                if str(registro.idUsuario) == str(id_usuario):
                    registro.delete()
                    return JsonResponse({'mensaje': 'Asistencia eliminado correctamente'})
                else:
                    return JsonResponse({'error': 'El usuario no puede eliminar este registro por que no le pertenece'}, status=400)
            else:
                return JsonResponse({'error': 'Se requiere un token de autenticación'}, status=400)
        except Asistencia.DoesNotExist:
            return JsonResponse({'error': 'El registro con es id no existe'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)},status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones DELETE'}, status=400)
    


@csrf_exempt
def obtener_asistencia(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idEvent = data.get('idEvento')
            registros = Asistencia.objects.filter(idEvento = idEvent)
            
            registros_json = []

            for registro in registros:
                registro_dict = {
                    'id': registro.id,
                    'idEvento': registro.idEvento,
                    'idUsuario':registro.idUsuario,
                    'nombreUsuario': obtener_nombre_de_usuario_por_id(registro.idUsuario),
                    'fechaIngreso': registro.fechaIngreso
                }
                registros_json.append(registro_dict)

            return JsonResponse({'registros': registros_json})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)


'''-----------------------------------ListadoCanciones-------------------------------------'''
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_listado(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idevent = data.get('idEvento')
            idasis = data.get('idAsistencia')
            nombrecancio = data.get('nombreCancion')
            artist = data.get('artista')
            albu = data.get('albun')
            duracio = data.get('duracion')
            linkFotoCancio = data.get('linkFotoCancion')
            fechaSolicitad = data.get('fechaSolicitada')
            estadoCancio = data.get('estadoCancion')
            linkReproducto = data.get('linkReproductor')

            
            # Crear un nuevo evento
            nueva_lista = ListadoCanciones.objects.create(
                idEvento=idevent,
                idAsistencia=idasis,
                nombreCancion=nombrecancio,
                artista=artist,
                albun=albu,
                duracion=duracio,
                linkFotoCancion=linkFotoCancio,
                fechaSolicitada=fechaSolicitad,
                estadoCancion=estadoCancio,
                linkReproductor=linkReproducto
            )
            
            # Retornar el ID del evento creado
            return JsonResponse({'id': nueva_lista.id})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)
    
@csrf_exempt
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def actualizar_listado(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            authorization_header = request.headers.get('Authorization')
            if authorization_header:
                # Separar el tipo de esquema de autenticación y el token
                _, token = authorization_header.split(None, 1)
                # Eliminar el prefijo 'Bearer ' si está presente en el token
                token = token.replace('Bearer ', '')
                # Ahora el token contiene solo el token sin el prefijo 'Bearer'
                id_usuario = obtenerIdUser(token)
                
                id_lista = data.get('idLista')
                estadoCancio = data.get('estadoCancion')
                
                # Verificar si el producto pertenece al establecimiento del usuario
                registro = ListadoCanciones.objects.get(id=id_lista)
                registro.estadoCancion = estadoCancio
                registro.save()
                return JsonResponse({'mensaje': 'Se actualizo correctamente'}, status=400)
            else:
                return JsonResponse({'error': 'Se requiere un token de autenticación'}, status=400)
        except ListadoCanciones.DoesNotExist:
            return JsonResponse({'error': 'El registro con es id no existe'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)},status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones PUT'}, status=400)
    



@csrf_exempt
def obtener_lista(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idEvent = data.get('idEvento')
            registros = ListadoCanciones.objects.filter(idEvento = idEvent)
            
            registros_json = []

            for registro in registros:
                registro_dict = {
                    'id': registro.id,
                    'idEvento': registro.idEvento,
                    'idAsistencia':registro.idAsistencia,
                    'nombreCancion':registro.nombreCancion,
                    'artista':registro.artista,
                    'albun':registro.albun,
                    'duracion':registro.duracion,
                    'linkFotoCancion':registro.linkFotoCancion,
                    'fechaSolicitada':registro.fechaSolicitada,
                    'estadoCancion':registro.estadoCancion,
                    'estadoCancion':registro.estadoCancion
                }
                registros_json.append(registro_dict)

            return JsonResponse({'registros': registros_json})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta peticiones POST'}, status=400)

'''----------------------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------'''
'''-------------------------------------funciones------------------------------------'''
'''----------------------------------------------------------------------------------'''

def obtenerIdUser(token):

    # Clave secreta utilizada para firmar el token (si es necesario)
    clave_secreta = "django-insecure-zl*jy15203f%uv9*(tmar=#-%yrk2(3lu^q9=zh^+#q864l1ue"

    # Decodificar el token
    try:
        decoded_token = jwt.decode(token, clave_secreta, algorithms=["HS256"])
        print("Token decodificado:", decoded_token)
        return decoded_token['user_id']
    except jwt.ExpiredSignatureError:
        print("El token ha expirado.")
    except jwt.InvalidTokenError:
        print("El token es inválido.")



def obtener_nombre_de_usuario_por_id(id_usuario):
    try:
        # Buscar el usuario por su ID
        User = get_user_model()
        usuario = User.objects.get(id=id_usuario)
        # Obtener el nombre del usuario
        nombre_usuario = usuario.first_name
        return nombre_usuario
    except User.DoesNotExist:
        # Manejar el caso en que no se encuentre el usuario
        return None


def obtener_establecimiento_de_usuario_por_id(id_usuario):
    try:
        # Buscar el usuario por su ID
        User = get_user_model()
        usuario = User.objects.get(id=id_usuario)
        # Obtener el nombre del usuario
        idevento = usuario.idEstablecimiento
        return idevento
    except User.DoesNotExist:
        # Manejar el caso en que no se encuentre el usuario
        return None
    
def obtener_numero_likes_evento(id_evento):
    try:
        registro = MegustaEventos.objects.filter(idEvento=id_evento).count()
        return registro
    except MegustaEventos.DoesNotExist:
        # Manejar el caso en que no se encuentre el usuario
        return 0
    
def obtener_numero_likes_establecimiento(id_establecimiento):
    try:
        registro = MegustaEstablecimiento.objects.filter(idEstablecimiento=id_establecimiento).count()
        return registro
    except MegustaEventos.DoesNotExist:
        # Manejar el caso en que no se encuentre el usuario
        return 0
def obtener_email_establecimiento(id_establecimiento):
    try:
        # Buscar el usuario por su ID
        User = get_user_model()
        usuario = User.objects.get(idEstablecimiento=id_establecimiento)
        # Obtener el nombre del usuario
        username = usuario.username
        return username
    except User.DoesNotExist:
        # Manejar el caso en que no se encuentre el usuario
        return None