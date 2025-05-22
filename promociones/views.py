from rest_framework import viewsets
from .models import Promocion
from .serializers import PromocionSerializer

class PromocionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows promociones to be viewed or edited.
    """
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer