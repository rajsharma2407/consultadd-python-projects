from django.shortcuts import render
from django.http import HttpResponse    
from .models import Employee

def main(request):
    context = {'one': 'one  '}
    return render(request, 'application/index.html', context)

def employees(request):
    output = Employee.objects.all()
    context = {'Employee': output}
    return render(request, 'application/employees.html', context)