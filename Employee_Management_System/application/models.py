from django.db import models

# Create your models here.

class Department(models.Model):
    department_id = models.IntegerField()
    department_name = models.CharField(max_length=100)
    def __str__(self):
        return self.department_name

class Employee(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    is_manager = models.BooleanField(default=False)