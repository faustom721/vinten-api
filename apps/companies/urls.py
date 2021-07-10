from rest_framework.routers import DefaultRouter

from apps.companies import views


router = DefaultRouter(trailing_slash=False)

router.register(r'companies', views.CompanyViewSet)
router.register(r'memberships', views.MembershipViewSet,
                basename='memberships')
router.register(r'clients', views.ClientViewSet, basename='clients')
