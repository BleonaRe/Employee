from django.contrib import admin
from employeeSystem.models import (Employee, Attendance, Schedule, PerformanceReport )


admin.site.register(Employee)

admin.site.register(Attendance)

admin.site.register(Schedule)

admin.site.register(PerformanceReport)

