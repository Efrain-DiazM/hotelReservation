from rest_framework import viewsets
from .models import Reserva
from .serializers import ReservaSerializer

from rest_framework.response import Response
from django.db import connection
from rest_framework import status
from rest_framework.views import APIView

class ReservaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reservas to be viewed or edited.
    """
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class HabitacionesDisponiblesWifiAPIView(APIView):
    def get(self, request):
        hotel_id = request.query_params.get('hotel')
        fecha_checkin = request.query_params.get('fecha_checkin')
        fecha_checkout = request.query_params.get('fecha_checkout')
        capacidad_minima = request.query_params.get('capacidad_minima')

        if not all([hotel_id, fecha_checkin, fecha_checkout, capacidad_minima]):
            return Response({'error': 'Faltan parámetros'}, status=status.HTTP_400_BAD_REQUEST)

        with connection.cursor() as cursor:
            cursor.callproc(
                'BuscarHabitacionesDisponiblesWifi',
                [hotel_id, fecha_checkin, fecha_checkout, capacidad_minima]
            )
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        return Response(results)

class PuntuacionMediaHotelAPIView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM vista_puntuacion_media_hotel;")
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        return Response(results, status=status.HTTP_200_OK)
    
class HabitacionesNuncaReservadasAPIView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM vista_habitaciones_nunca_reservadas;")
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        return Response(results, status=status.HTTP_200_OK)

class IngresosHotelUltimoMesAPIView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM vista_ingresos_hotel_ultimo_mes;")
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        return Response(results, status=status.HTTP_200_OK)

class PromocionesActivasConUsoAPIView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM vista_promociones_activas_con_uso;")
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        return Response(results, status=status.HTTP_200_OK)
    

class CrearReservaConFacturaAPIView(APIView):
    def post(self, request):
        data = request.data
        required_fields = [
            'hotel_id', 'habitacion_id', 'cliente_id', 'fecha_checkin', 'fecha_checkout',
            'numero_adultos', 'numero_ninos', 'empleado_checkin_id'
        ]
        for field in required_fields:
            if field not in data:
                return Response({'error': f'Falta el campo {field}'}, status=status.HTTP_400_BAD_REQUEST)

        hotel_id = data['hotel_id']
        habitacion_id = data['habitacion_id']
        cliente_id = data['cliente_id']
        fecha_checkin = data['fecha_checkin']
        fecha_checkout = data['fecha_checkout']
        numero_adultos = data['numero_adultos']
        numero_ninos = data['numero_ninos']
        empleado_checkin_id = data['empleado_checkin_id']
        codigo_promo = data.get('codigo_promo', None)

        try:
            with connection.cursor() as cursor:
                # Prepara los parámetros de salida
                cursor.execute("SET @reserva_id = 0;")
                cursor.execute("SET @factura_id = 0;")
                # Llama al procedimiento
                cursor.callproc(
                    'CrearReservaConFactura',
                    [
                        hotel_id, habitacion_id, cliente_id, fecha_checkin, fecha_checkout,
                        numero_adultos, numero_ninos, empleado_checkin_id, codigo_promo,
                        '@reserva_id', '@factura_id'
                    ]
                )
                # Recupera los valores de salida
                cursor.execute("SELECT @reserva_id AS reserva_id, @factura_id AS factura_id;")
                result = cursor.fetchone()
                reserva_id, factura_id = result
            return Response({'reserva_id': reserva_id, 'factura_id': factura_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)    

class EstadoActualHabitacionesAPIView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM vista_ocupacion_actual_por_hotel_completa;")
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        return Response(results, status=status.HTTP_200_OK)