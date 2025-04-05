from django.contrib import admin
from django.urls import path, include
from employeeSystem.urls import router
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from employeeSystem import views

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Employee Management API",
        default_version="v1",
        description="API documentation for Employee Management System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", views.login_view, name="login"),
    path("home/", views.home, name="home"),
    path("register/", views.register_view, name="register"),
    path("admin/", admin.site.urls),
    path("logout/", views.logout_view, name="logout"),
    path("", include("employeeSystem.urls")),
    # Swagger UI
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # Redoc UI
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
