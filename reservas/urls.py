from rest_framework.routers import DefaultRouter
from .views import ReservaViewSet, HabitacionesDisponiblesWifiAPIView, PuntuacionMediaHotelAPIView, HabitacionesNuncaReservadasAPIView, IngresosHotelUltimoMesAPIView, PromocionesActivasConUsoAPIView, CrearReservaConFacturaAPIView, EstadoActualHabitacionesAPIView
from django.urls import path

router = DefaultRouter()
router.register(r'reservas', ReservaViewSet, basename='reserva')
urlpatterns = router.urls

urlpatterns += [
    path('disponibles-wifi/', HabitacionesDisponiblesWifiAPIView.as_view(), name='habitaciones-disponibles-wifi'),
    path('puntuacion-media/', PuntuacionMediaHotelAPIView.as_view(), name='puntuacion-media-hotel'),
    path('nunca-reservadas/', HabitacionesNuncaReservadasAPIView.as_view(), name='habitaciones-nunca-reservadas'),
    path('ingresos-ultimo-mes/', IngresosHotelUltimoMesAPIView.as_view(), name='ingresos-hotel-ultimo-mes'),
    path('activas-con-uso/', PromocionesActivasConUsoAPIView.as_view(), name='promociones-activas-con-uso'),
    path('reservar-con-factura/', CrearReservaConFacturaAPIView.as_view(), name='reservar-con-factura'),
    path('estado-actual-habitaciones/', EstadoActualHabitacionesAPIView.as_view(), name='estado-actual-habitaciones'),
]