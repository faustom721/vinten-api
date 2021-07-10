from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.people import views


router = DefaultRouter(trailing_slash=False)

router.register(r'users', views.UserViewSet)
router.register(r'me',
                views.CurrentUserViewSet, basename='current_user')

urls = [
    path('set_last_used_company/', views.SetLastUsedCompanyView.as_view()),
] + router.urls
