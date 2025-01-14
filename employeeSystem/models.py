from django.db import models

# Create your models here
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("hr", "HR"),
        ("manager", "Manager"),
        ("employee", "Employee"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="employee")

    # Resolve clashes by setting related_name
    groups = models.ManyToManyField(
        Group,
        related_name="employee_system_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="employee_system_user_permissions_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )


# Employee model
class Employee(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# Attendance model
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10, choices=[("present", "Present"), ("absent", "Absent")]
    )

    def __str__(self):
        return f"{self.employee.name} - {self.date}"


# Performance Report model
class PerformanceReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tasks_completed = models.IntegerField()
    attendance_score = models.FloatField()
    evaluation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.name} - {self.evaluation_date}"


# Schedule model
class Schedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift_start = models.TimeField()
    shift_end = models.TimeField()

    def __str__(self):
        return f"{self.employee.name} - {self.shift_start} to {self.shift_end}"
