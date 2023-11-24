from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include("modules.accounts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

project_name = settings.PROJECT_NAME

admin.site.site_header = f"{project_name} Admin"
admin.site.site_title = f"{project_name} Admin Portal"
admin.site.index_title = f"Welcome to {project_name} Portal"
