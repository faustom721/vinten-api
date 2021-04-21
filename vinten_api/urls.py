from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from people.urls import router as people_router

admin.site.site_header = "Vinten Admin"
admin.site.site_title = "Vinten Admin"
admin.site.index_title = "Vinten Admin Mainpage"

router = DefaultRouter()

urlpatterns = [
    path('', admin.site.urls),
    path('', include(people_router.urls))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(urlpatterns)
