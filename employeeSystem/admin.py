from django.contrib import admin
from employeeSystem.models import (Employee, Attendance, Schedule, PerformanceReport, Goals, Projects, Surveys, Holidays, Assets )


admin.site.register(Employee)

admin.site.register(Attendance)

admin.site.register(Schedule)

admin.site.register(PerformanceReport)

admin.site.register(Projects)

admin.site.register(Goals)

admin.site.register(Surveys)

admin.site.register(Holidays)

admin.site.register(Assets)