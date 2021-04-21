from rest_framework.routers import DefaultRouter

from people import views

# Create a router and register our viewsets with it.

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'roles', views.RoleViewSet)
