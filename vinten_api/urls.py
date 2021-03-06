from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

from apps.people.serializers import CustomJWTSerializer
from apps.people.urls import urls as people_urls
from apps.companies.urls import router as companies_router

admin.site.site_header = "Vinten Admin"
admin.site.site_title = "Vinten Admin"
admin.site.index_title = "Vinten Admin Mainpage"


urlpatterns = [
    path('', admin.site.urls),

    path('token/', jwt_views.TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(people_urls)),
    path('', include(companies_router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
