from django.db import models
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
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
    date = models.DateField(auto_now_add=True)  # Vendoset automatikisht
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
from django.db import models

class Goals(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=200)
    description = models.TextField()
    target_date = models.DateField()
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return self.goal_name


class Projects(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])

    def __str__(self):
        return self.project_name


class Surveys(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    survey_title = models.CharField(max_length=200)
    survey_date = models.DateField()
    feedback = models.TextField()

    def __str__(self):
        return self.survey_title


class Assets(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=200)
    asset_type = models.CharField(max_length=100)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    condition = models.CharField(max_length=100, choices=[('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')])

    def __str__(self):
        return self.asset_name


class Holidays(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    holiday_name = models.CharField(max_length=200)
    holiday_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.holiday_name


# Activity model
class Activity(models.Model):
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

# Notification model
class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title
