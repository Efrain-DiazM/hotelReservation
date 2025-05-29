from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, RolViewSet

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet, basename='empleado')
router.register(r'roles', RolViewSet, basename='rol')

urlpatterns = router.urls