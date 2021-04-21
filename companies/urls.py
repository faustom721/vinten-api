from rest_framework.routers import DefaultRouter

from companies import views


router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
