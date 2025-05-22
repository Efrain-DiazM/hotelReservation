from rest_framework import viewsets
from .models import Empleado
from .serializers import EmpleadoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows empleados to be viewed or edited.
    """
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
