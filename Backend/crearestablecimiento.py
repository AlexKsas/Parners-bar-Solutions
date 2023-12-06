import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')  # Ajusta 'proyecto.settings' al nombre de tu módulo de configuración Django
django.setup()

from app.models import Establecimientos

def create_establecimiento():
    id_establecimiento = '2'
    nombre = 'RAKATA'
    latitud = '60.456'
    longitud = '95.789'
    id_horario = ''

    establecimiento, created = Establecimientos.objects.get_or_create(
        id=id_establecimiento,
        defaults={
            'NombreEstablecimiento': nombre,
            'Latitud': latitud,
            'Longitud': longitud,
            'idHorario': id_horario
        }
    )
    if created:
        print(f'Establecimiento "{nombre}" creado con éxito.')
    else:
        print(f'El establecimiento "{nombre}" ya existe.')

if __name__ == '__main__':
    create_establecimiento()
