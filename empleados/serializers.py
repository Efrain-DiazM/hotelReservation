from rest_framework import serializers
from .models import Empleado, Rol

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'