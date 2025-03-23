from rest_framework import serializers
from employeeSystem.models import (
    Employee,
    Attendance,
    PerformanceReport,
    Schedule,
    Goals,
    Projects,
    Surveys,
    Holidays,
    Assets
)

# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = ["id"]

# Attendance Serializer
class AttendanceSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = Attendance
        fields = "__all__"
        read_only_fields = ["id", "date"]

# Performance Report Serializer
class PerformanceReportSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = PerformanceReport
        fields = "__all__"
        read_only_fields = ["id", "evaluation_date"]

# Schedule Serializer
class ScheduleSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = Schedule
        fields = "__all__"
        read_only_fields = ["id"]

# Goals Serializer
class GoalsSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = Goals
        fields = ["id", "employee", "goal_name", "description", "target_date", "achieved"]

# Projects Serializer
class ProjectsSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = Projects
        fields = ["id", "employee", "project_name", "description", "start_date", "end_date", "status"]

# Surveys Serializer
class SurveysSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = Surveys
        fields = ["id", "employee", "survey_title", "survey_date", "feedback"]

# Assets Serializer
class AssetsSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = Assets
        fields = ["id", "employee", "asset_name", "asset_type", "issue_date", "return_date", "condition"]

# Holidays Serializer
class HolidaysSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = Holidays
        fields = ["id", "employee", "holiday_name", "holiday_date", "is_approved"]
