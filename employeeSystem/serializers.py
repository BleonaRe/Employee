from employeeSystem.models import (
    Employee,
    Attendance,
    PerformanceReport,
    Schedule,
)
from rest_framework import serializers

# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = ["id"]

# Attendance Serializer
class AttendanceSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()  # Shfaq emrin e punonjësit në vend të ID-së

    class Meta:
        model = Attendance
        fields = "__all__"
        read_only_fields = ["id", "date"]  # `date` vendoset automatikisht

# Performance Report Serializer
class PerformanceReportSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = PerformanceReport
        fields = "__all__"
        read_only_fields = ["id", "evaluation_date"]  # `evaluation_date` vendoset automatikisht

# Schedule Serializer
class ScheduleSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = Schedule
        fields = "__all__"
        read_only_fields = ["id"]
