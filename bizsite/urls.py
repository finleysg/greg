from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views as core_views
from documents import views as document_views
from messaging import views as messaging_views
from content import views as content_views

admin.site.site_header = "Northern Summit Construction Administration"

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"photos", document_views.PhotoViewSet, "photos")
router.register(r"page-content", content_views.PageContentViewSet, "page-content")
router.register(r"settings", core_views.SiteSettingsViewSet, "settings")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/contact/", messaging_views.contact_message),
    path("auth/", include("djoser.urls")),
    path("auth/token/login/", core_views.TokenCreateView.as_view(), name="login"),
    path("auth/token/logout/", core_views.TokenDestroyView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
