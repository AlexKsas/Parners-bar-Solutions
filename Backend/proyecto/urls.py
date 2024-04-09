"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from app import views

urlpatterns = [
    path('obtenereventos/',views.obtener_registros_eventos),
    path('admin/', admin.site.urls),
    path('establecimientos/', views.obtener_registros_establecimientos),
    path('establecimientoscerca/', views.consulta_discotecas_cercanas),
    path('crearevento/', views.crear_evento),
    path('crearmegusta/', views.crear_megusta_evento),
    path('crearcomentario/', views.crear_comentario_evento),
    path('eliminarmegusta/', views.eliminar_megusta_evento),
    path('eliminarcomentario/', views.eliminar_comentario_evento),
    path('consultarmegusta/', views.obtener_megusta_evento),
    path('consultarcomentarios/', views.obtener_comentarios_evento),
    path('crearestablecimientos/',views.crear_registro_establecimientos),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener token de acceso
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Renovar token de acceso
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verificar token
]
