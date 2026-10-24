"""Корневая маршрутизация проекта."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("orders/", include("apps.orders.urls")),
    path("", include("apps.core.urls")),
]

if settings.DEBUG:
    # В разработке отдаём загруженные файлы из MEDIA_ROOT
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
