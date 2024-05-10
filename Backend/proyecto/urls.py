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
    path('userinfo/',views.consultar_usuario),
    path('infoestableciminetocel/',views.obtener_discotecaCel),
    path('infoevento/',views.obtener_evento),
    path('infoestableciminetopc/',views.obtener_discotecaPc),
    path('createuser/',views.crear_usuario),
    path('admin/', admin.site.urls),
    path('establecimientos/', views.obtener_registros_establecimientos),
    path('establecimientoscerca/', views.consulta_discotecas_cercanas),
    path('crearevento/', views.crear_evento),
    path('like/', views.crear_megusta_evento),
    path('likeestablecimiento/', views.crear_megusta_establecimiento),
    path('crearcomentario/', views.crear_comentario_evento),
    path('eliminarmegusta/', views.eliminar_megusta_evento),
    path('eliminarcomentario/', views.eliminar_comentario_evento),
    path('consultarmegusta/', views.obtener_megusta_evento),
    path('consultarmegustaestablecimiento/', views.obtener_megusta_establecimiento),
    path('consultarcomentarios/', views.obtener_comentarios_evento),
    path('crearestablecimientos/',views.crear_discoteca),
    path('eventsbyestablecimiento/',views.obtener_registros_eventos_por_establecimiento),
    path('updateevent/',views.actualizar_evento),
    path('createproduct/',views.crear_producto),
    path('deleteproduct/',views.eliminar_producto),
    path('obtenerproductoscel/',views.obtener_productosCel),
    path('obtenerproductospc/',views.obtener_productosPc),
    path('createasistencia/',views.crear_asistencia),
    path('deleteasistencia/',views.eliminar_asistencia),
    path('obtenerasistencia/',views.obtener_asistencia),
    path('createlistacancion/',views.crear_listado),
    path('updatelistacancion/',views.actualizar_listado),
    path('obtenerlistacancion/',views.obtener_lista),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener token de acceso
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Renovar token de acceso
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verificar token
]
