import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')  # Reemplaza 'api.settings' con la ruta a tu archivo de configuración de Django
django.setup()

def create_user():
    User = get_user_model()
    username = 'bar3@gmail.com'  # Nombre de usuario deseado
    password = 'bar1234'  # Contraseña deseada
    cedula = '100243838'
    celular = '31154874'
    user, created = User.objects.get_or_create(username=username, 
                                               defaults={
            'cedula': cedula,
            'celular': celular
        })
    if created:
        user.set_password(password)
        user.save()
        print(f'Usuario "{username}" creado con éxito.')
    else:
        print(f'El usuario "{username}" ya existe.')

if __name__ == '__main__':
    create_user()
