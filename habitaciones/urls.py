from rest_framework.routers import DefaultRouter
from .views import HabitacionViewSet

router = DefaultRouter()
router.register(r'habitaciones', HabitacionViewSet, basename='habitacion')
urlpatterns = router.urls