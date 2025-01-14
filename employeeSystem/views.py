from django.shortcuts import render

# Create your views here.
from employeeSystem.models import (
    Employee,
    Attendance,
    PerformanceReport,
    Schedule,
)
from employeeSystem.serializers import (
    EmployeeSerializer,
    AttendanceSerializer,
    PerformanceReportSerializer,
    ScheduleSerializer,
)
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


# ViewSets
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [AllowAny]


class PerformanceReportViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReport.objects.all()
    serializer_class = PerformanceReportSerializer
    permission_classes = [AllowAny]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [AllowAny]
