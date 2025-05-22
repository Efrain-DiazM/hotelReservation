from rest_framework import viewsets
from .models import Habitacion
from .serializers import HabitacionSerializer

class HabitacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows habitaciones to be viewed or edited.
    """
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer