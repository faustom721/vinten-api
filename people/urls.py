from rest_framework.routers import DefaultRouter

from people import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
