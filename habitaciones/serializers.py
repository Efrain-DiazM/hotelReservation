from rest_framework import serializers
from .models import Habitacion, TipoHabitacion
from hoteles.serializers import HotelSerializer

class TipoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = '__all__'
        
class HabitacionSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)
    tipo_habitacion = TipoHabitacionSerializer(read_only=True)
    class Meta:
        model = Habitacion
        fields = '__all__'

class HabitacionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'