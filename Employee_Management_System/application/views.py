from django.shortcuts import render
from django.http import HttpResponse    
from .models import Employee, Department
import json

def main(request):
    context = {'one': 'one'}
    return render(request, 'application/index.html', context)

def employees(request):
    print(request.method)
    output = Employee.objects.all()
    context = {'Employee': output}
    return render(request, 'application/employees.html', context)

def createEmployees(request):
    x = json.loads(request.body.decode())
    y = Employee(employee_id = x['employee_id'], employee_name = x['employee_name'], department_name = Department.objects.get(department_id = x['department_name']), is_manager = x['is_manager'])
    y.save()
    return employees(request)

def department(request):
    output = Department.objects.all()
    context = {'Department': output}
    return render(request, 'application/department.html', context)