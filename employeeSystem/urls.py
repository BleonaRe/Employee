from employeeSystem.views import (
    EmployeeViewSet,
    AttendanceViewSet,
    PerformanceReportViewSet,
    ScheduleViewSet,
)

# Router
router = routers.DefaultRouter()
router.register(r"employees", EmployeeViewSet)
router.register(r"attendance", AttendanceViewSet)
router.register(r"performance-reports", PerformanceReportViewSet)
router.register(r"schedules", ScheduleViewSet)
