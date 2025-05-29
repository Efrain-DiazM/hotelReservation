from rest_framework import viewsets
from .models import Habitacion, TipoHabitacion
from .serializers import HabitacionSerializer, HabitacionCreateSerializer, TipoHabitacionSerializer
from servicios.models import Servicio
from reservas.models import Reserva
from promociones.models import Promocion

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from datetime import datetime

class HabitacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows habitaciones to be viewed or edited.
    """
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class HabitacionCreateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows habitaciones to be viewed or edited.
    """
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionCreateSerializer

class TipoHabitacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tipos de habitaciones to be viewed or edited.
    """
    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer

def buscar_habitaciones_disponibles(hotel_id, fecha_inicio, fecha_fin, capacidad_minima):
    # 1. Habitaciones del hotel con capacidad mínima
    habitaciones = Habitacion.objects.filter(
        hotel_id=hotel_id,
        tipo_habitacion__capacidad_max__gte=capacidad_minima,
        estado='disponible'
    )

    # 2. Excluir habitaciones reservadas en el rango de fechas
    habitaciones = habitaciones.exclude(
        reserva__fecha_checkin__lt=fecha_fin,
        reserva__fecha_checkout__gt=fecha_inicio,
        reserva__estado_reserva__in=['Pendiente', 'Confirmada', 'En curso']
    )

    # 3. Filtrar habitaciones que tengan WiFi Gratis
    wifi = Servicio.objects.get(nombre_servicio__iexact='WiFi Gratis')
    habitaciones = habitaciones.filter(roomservicio__servicio=wifi)

    return habitaciones

class HabitacionesDisponiblesAPIView(APIView):
    def get(self, request):
        # Cambia los nombres para que coincidan con el frontend
        hotel_id = request.query_params.get('hotel')
        fecha_checkin = request.query_params.get('fecha_checkin')
        fecha_checkout = request.query_params.get('fecha_checkout')
        capacidad_minima = request.query_params.get('capacidad_minima')

        if not all([hotel_id, fecha_checkin, fecha_checkout, capacidad_minima]):
            return Response({'error': 'Faltan parámetros'}, status=status.HTTP_400_BAD_REQUEST)

        habitaciones = Habitacion.objects.filter(
            hotel_id=hotel_id,
            tipo_habitacion__capacidad_max__gte=capacidad_minima,
            estado='disponible'
        )

        # Excluir habitaciones reservadas en el rango de fechas
        habitaciones = habitaciones.exclude(
            reservas__fecha_checkin__lt=fecha_checkout,
            reservas__fecha_checkout__gt=fecha_checkin,
            reservas__estado_reserva__in=['Pendiente', 'Confirmada', 'En curso']
        )

        # Filtrar habitaciones que tengan WiFi Gratis
        try:
            wifi = Servicio.objects.get(nombre_servicio__iexact='WiFi Gratis')
            habitaciones = habitaciones.filter(roomservicio__servicio=wifi)
        except Servicio.DoesNotExist:
            habitaciones = habitaciones.none()

        serializer = HabitacionSerializer(habitaciones, many=True)
        return Response(serializer.data)
    
class ValidarDisponibilidadYCostoAPIView(APIView):
    def post(self, request):
        habitacion_id = request.data.get('habitacion')
        fecha_checkin = request.data.get('fecha_checkin')
        fecha_checkout = request.data.get('fecha_checkout')
        promocion_codigo = request.data.get('promocion', None)

        if not all([habitacion_id, fecha_checkin, fecha_checkout]):
            return Response({'error': 'Faltan parámetros'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            habitacion = Habitacion.objects.get(id=habitacion_id)
        except Habitacion.DoesNotExist:
            return Response({'error': 'Habitación no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        # Validar disponibilidad
        reservas_conflictivas = Reserva.objects.filter(
            habitacion=habitacion,
            fecha_checkin__lt=fecha_checkout,
            fecha_checkout__gt=fecha_checkin,
            estado_reserva__in=['Pendiente', 'Confirmada', 'En curso']
        )
        disponible = not reservas_conflictivas.exists()

        # Calcular costo
        nights = (datetime.strptime(fecha_checkout, "%Y-%m-%d") - datetime.strptime(fecha_checkin, "%Y-%m-%d")).days
        costo_base = nights * float(habitacion.precio_por_noche)
        descuento = 0
        promo_info = None

        if promocion_codigo:
            try:
                promo = Promocion.objects.get(codigo_promo=promocion_codigo, activa=True)
                promo_info = {
                    "descripcion": promo.descripcion,
                    "descuento_porcentaje": float(promo.descuento_porcentaje),
                    "descuento_fijo": float(promo.descuento_fijo)
                }
                if promo.descuento_porcentaje > 0:
                    descuento = (costo_base * promo.descuento_porcentaje) / 100
                elif promo.descuento_fijo > 0:
                    descuento = promo.descuento_fijo
            except Promocion.DoesNotExist:
                return Response({'error': 'Código promocional inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        costo_total = max(costo_base - descuento, 0)

        return Response({
            'disponible': disponible,
            'costo_total': round(costo_total, 2),
            'promo_info': promo_info
        })