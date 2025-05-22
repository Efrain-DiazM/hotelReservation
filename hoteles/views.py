from rest_framework import viewsets
from .models import Hotel
from .serializers import HotelSerializer

class HotelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hoteles to be viewed or edited.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer