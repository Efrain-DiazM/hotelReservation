from rest_framework import viewsets
from .models import Reserva
from .serializers import ReservaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reservas to be viewed or edited.
    """
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer