from rest_framework.routers import DefaultRouter
from .views import HabitacionViewSet, TipoHabitacionViewSet, HabitacionCreateViewSet, HabitacionesDisponiblesAPIView, ValidarDisponibilidadYCostoAPIView
from django.urls import path

router = DefaultRouter()
router.register(r'habitaciones', HabitacionViewSet, basename='habitacion')
router.register(r'CrearHabitaciones', HabitacionCreateViewSet, basename='habitacionCrear')
router.register(r'tiposHabitacion', TipoHabitacionViewSet, basename='tipo_habitacion')
urlpatterns = router.urls + [
    path('disponibles/', HabitacionesDisponiblesAPIView.as_view(), name='habitaciones-disponibles'),
    path('validar-disponibilidad-costo/', ValidarDisponibilidadYCostoAPIView.as_view(), name='validar-disponibilidad-costo'),
]