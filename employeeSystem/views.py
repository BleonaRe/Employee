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
 
# views.py
from django.shortcuts import render
from .models import Employee, Attendance, PerformanceReport, Schedule

# Krijo një view për homepage që merr të dhënat nga modelet
def home(request):
    # Merr të dhënat nga modelet
    employees = Employee.objects.all()
    attendances = Attendance.objects.all()
    performance_reports = PerformanceReport.objects.all()
    schedules = Schedule.objects.all()

    # Dërgo të dhënat në template
    return render(request, 'employeeSystem/home.html', {
        'employees': employees,
        'attendances': attendances,
        'performance_reports': performance_reports,
        'schedules': schedules
    })
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required  # Ky dekorator siguron që vetëm përdoruesit e loguar mund të aksesorojnë këtë view
def home(request):
    # Merr të dhënat nga modelet
    employees = Employee.objects.all()
    attendances = Attendance.objects.all()
    performance_reports = PerformanceReport.objects.all()
    schedules = Schedule.objects.all()

    # Dërgo të dhënat në template
    return render(request, 'employeeSystem/login.html', {
        'employees': employees,
        'attendances': attendances,
        'performance_reports': performance_reports,
        'schedules': schedules
    })# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'admin':  # Kontrollo nëse është admin
                return redirect('admin_dashboard')  # Drejtoje në dashboard-in e adminit
            else:
                return redirect('home')  # Përdoruesit të tjerë drejtohen në homepage
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'employeeSystem/login.html')

from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'admin':  # Kontrollo nëse është admin
                return redirect('admin_dashboard')  # Drejtoje në dashboard-in e adminit
            else:
                return redirect('home')  # Përdoruesit të tjerë drejtohen në homepage
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'employeeSystem/login.html')

from .forms import RegisterForm
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Shendos passwordin
            user.save()

            # Autentifikim i përdoruesit pas regjistrimit
            login(request, user)

            messages.success(request, "Account created successfully!")
            return redirect('home')  # Mund të ndryshoni redirektimin sipas nevojës
        else:
            messages.error(request, "There was an error with your form.")
    else:
        form = RegisterForm()

    return render(request, 'employeeSystem/register.html', {'form': form})


