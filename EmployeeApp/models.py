from django.db import models

# Create your models here.

# Stores Department Data
class Department(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

# Stores the Employee Data
class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    ImageFileName = models.CharField(max_length=100)