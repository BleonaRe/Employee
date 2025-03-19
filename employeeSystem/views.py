from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from .forms import RegisterForm
from .models import Employee, Attendance, PerformanceReport, Schedule
from .serializers import (
    EmployeeSerializer, AttendanceSerializer, PerformanceReportSerializer, ScheduleSerializer
)
from django.contrib.auth.decorators import login_required


@login_required  # Kjo e bën të detyrueshëm login-in për të hyrë në home
def home(request):
    return render(request, 'employeeSystem/home.html')


# ✅ Home view (Ridrejton në login nëse përdoruesi nuk është i kyçur)
def home(request):
    if not request.user.is_authenticated:  # Kontrollo nëse përdoruesi nuk është i kyçur
        return redirect('login')  # Ridrejto në faqen e login-it

    employees = Employee.objects.all()
    attendances = Attendance.objects.all()
    performance_reports = PerformanceReport.objects.all()
    schedules = Schedule.objects.all()

    return render(request, 'employeeSystem/home.html', {
        'employees': employees,
        'attendances': attendances,
        'performance_reports': performance_reports,
        'schedules': schedules
    })

# ✅ Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # Pas login-it, ridrejto në home
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'employeeSystem/login.html')

# ✅ Register View
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Enkripto passwordin
            user.save()

            # Kyç përdoruesin automatikisht pas regjistrimit
            login(request, user)

            messages.success(request, "Account created successfully!")
            return redirect('home')  # Pas regjistrimit, ridrejto në home
        else:
            messages.error(request, "There was an error with your form.")
    else:
        form = RegisterForm()

    return render(request, 'employeeSystem/register.html', {'form': form})

# ✅ Django REST Framework ViewSets për API
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class PerformanceReportViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReport.objects.all()
    serializer_class = PerformanceReportSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
