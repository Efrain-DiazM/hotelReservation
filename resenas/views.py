from rest_framework import viewsets
from .models import Resena
from .serializers import ResenaSerializer

class ResenaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reseñas to be viewed or edited.
    """
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer