from rest_framework.routers import DefaultRouter

from apps.companies import views


router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'memberships', views.MembershipViewSet,
                basename='memberships')
