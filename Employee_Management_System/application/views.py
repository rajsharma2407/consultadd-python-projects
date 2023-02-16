from django.shortcuts import render
from django.http import HttpResponse    
from .models import Employee, Department

def main(request):
    context = {'one': 'one  '}
    return render(request, 'application/index.html', context)

def employees(request):
    output = Employee.objects.all()
    context = {'Employee': output}
    return render(request, 'application/employees.html', context)

def createEmployees(request):
    print(request.body)
    return HttpResponse(request)

def department(request):
    output = Department.objects.all()
    context = {'Department': output}
    return render(request, 'application/department.html', context)