# employeeSystem/urls.py
from rest_framework import routers
from django.urls import path, include  # Importo 'path' dhe 'include'
from .views import (
    EmployeeViewSet,
    AttendanceViewSet,
    PerformanceReportViewSet,
    ScheduleViewSet,
)

router = routers.DefaultRouter()
router.register(r"employees", EmployeeViewSet)
router.register(r"attendance", AttendanceViewSet)
router.register(r"performance-reports", PerformanceReportViewSet)
router.register(r"schedules", ScheduleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Sigurohuni që ky rresht është aktivizuar
]
