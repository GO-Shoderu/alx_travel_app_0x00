from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import JsonResponse

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel App API",
        default_version="v1",
        description="Swagger documentation for alx_travel_app",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("alx_travel_app.listings.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]

def root_view(request):
    return JsonResponse({"message": "ALX Travel App API is running 🚀"})

urlpatterns = [
    path("", root_view, name="root"),
    path("admin/", admin.site.urls),
]
