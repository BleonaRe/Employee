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
    employee_list,
    employee_create,
    attendance_add,
    attendance_list,
)

router = routers.DefaultRouter()
# router.register(r"employees", EmployeeViewSet)
# router.register(r"attendance", AttendanceViewSet)
router.register(r"performance-reports", PerformanceReportViewSet)
router.register(r"schedules", ScheduleViewSet)
router.register(r"goals", GoalViewSet)
router.register(r"holidays", HolidayViewSet)
router.register(r"surveys", SurveyViewSet)
router.register(r"projects", ProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("employees/", employee_list, name="employee_list"),
    path("employees/new/", employee_create, name="employee_create"),
    path("attendance/", attendance_list, name="attendance_list"),
    path("attendance/add/", attendance_add, name="attendance_add"),
]
