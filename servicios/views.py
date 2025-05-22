from rest_framework import viewsets
from .models import Servicio
from .serializers import ServicioSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows servicios to be viewed or edited.
    """
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer