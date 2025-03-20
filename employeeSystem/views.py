from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from rest_framework import viewsets
from .forms import RegisterForm
from .models import Employee, Attendance, PerformanceReport, Schedule, Activity, Notification
from .serializers import (
    EmployeeSerializer, AttendanceSerializer, PerformanceReportSerializer, ScheduleSerializer
)

# Home view për përdorues të kyçur
@login_required
def home(request):
    # Statistikat dhe informacionet për punonjësit dhe aktivitetet
    total_employees = Employee.objects.count()
    total_attendance = Attendance.objects.filter(date=timezone.now().date()).count()  # Filtrimi për ditën e sotme
    recent_activity = Activity.objects.all().order_by('-timestamp')[:5]  # Aktivitetet më të fundit

    context = {
        'total_employees': total_employees,
        'total_attendance': total_attendance,
        'recent_activity': recent_activity,
    }

    return render(request, 'employeeSystem/home.html', context)

# Login View
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

# Register View
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

# Logout View
def logout_view(request):
    logout(request)  # Ky do të kryejë logout
    return redirect('login')  # Pas logout, përdoruesi drejtohet në faqen e login-it

# Django REST Framework ViewSets për API
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
