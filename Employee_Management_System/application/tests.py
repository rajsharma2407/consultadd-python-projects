from django.test import TestCase

from .models import Employee, Department
# Create your tests here.   
class QuestionModelTests(TestCase):

    def test_employee_without_department(self):
        employees = Employee.objects.all()
        departments = Department.objects.all()
        print(len(departments))
        print(len(employees))
        for emp in employees:
            print(emp)