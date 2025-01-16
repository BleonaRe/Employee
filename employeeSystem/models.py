from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Modeli i personalizuar User
class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("hr", "HR"),
        ("manager", "Manager"),
        ("employee", "Employee"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="employee")

    # Avoid clashes by setting related_name
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


# Modeli Employee
class Employee(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# Modeli Attendance
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10, choices=[("present", "Present"), ("absent", "Absent")]
    )

    def __str__(self):
        return f"{self.employee.name} - {self.date}"


# Modeli PerformanceReport
class PerformanceReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tasks_completed = models.IntegerField()
    attendance_score = models.FloatField()
    evaluation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.name} - {self.evaluation_date}"


# Modeli Schedule
class Schedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift_start = models.TimeField()
    shift_end = models.TimeField()

    def __str__(self):
        return f"{self.employee.name} - {self.shift_start} to {self.shift_end}"


# Modeli UserConnection
class UserConnection(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="connections_initiated")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="connections_received")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user1.username} connected to {self.user2.username}"
