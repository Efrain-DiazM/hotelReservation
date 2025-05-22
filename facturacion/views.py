from rest_framework import viewsets
from .models import Factura
from .serializers import FacturaSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows facturas to be viewed or edited.
    """
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer