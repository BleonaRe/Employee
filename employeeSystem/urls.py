# employeeSystem/urls.py
from rest_framework import routers
from django.urls import path, include  # Importo 'path' dhe 'include'
from .views import (
    EmployeeViewSet,
    AttendanceViewSet,
    PerformanceReportViewSet,
    ScheduleViewSet,
    GoalViewSet,
    ProjectViewSet,
    SurveyViewSet,
    HolidayViewSet,
)

router = routers.DefaultRouter()
router.register(r"employees", EmployeeViewSet)
router.register(r"attendance", AttendanceViewSet)
router.register(r"performance-reports", PerformanceReportViewSet)
router.register(r"schedules", ScheduleViewSet)
router.register(r"goals",GoalViewSet)
router.register(r"holidays",HolidayViewSet)
router.register(r"surveys",SurveyViewSet)
router.register(r"projects",ProjectViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Sigurohuni që ky rresht është aktivizuar
]
