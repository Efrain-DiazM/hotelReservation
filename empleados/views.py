from rest_framework import viewsets
from .models import Empleado, Rol
from .serializers import EmpleadoSerializer, RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows empleados to be viewed or edited.
    """
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
