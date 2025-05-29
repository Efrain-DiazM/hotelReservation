from django.contrib import admin
from .models import Servicio, HotelServicio, RoomServicio

admin.site.register(Servicio)
admin.site.register(HotelServicio)
admin.site.register(RoomServicio)