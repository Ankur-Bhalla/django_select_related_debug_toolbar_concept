# Example of join (select_related) i.e., one to many relation (Returns a QuerySet that
# will “follow” foreign-key relationships)

# Also use of in-built django debug toolbar
# Explain the problems with the default accessing method and specifically about the n+1 query problem
# in Django ORM. Then, we will fix the n+1 problem using Django select_related.

# from django.shortcuts import render
from .models import Department, Employee
from django.http import HttpResponse


# Create your views here.
def home(request):
    # Fetching all employees and printing their name and department

    # Run 1 ->
    # no. of queries will be 2 (mandatory ignore it) and 7 (department table n=7) + 1 (employee table n=1)
    # = 8 (n+1 = 8 queries in total)
    # employees = Employee.objects.all()

    # Run 2 ->
    # no. of queries will be 2 (mandatory ignore it) and 1 (join query) = 1 (so n+1 = 8 queries has been
    # replaced by 1 join query)
    employees = Employee.objects.all().select_related('department')

    # print(employees)  # comment this if not commented one more query will appear from employee table
    for employee in employees:
        print(employee.name, employee.department.name)

    # comment below statement to get error so that django debug toolbar will appear which will show
    # query execution time in milliseconds.
    # return HttpResponse("SQL queries and records successfully printed on terminal. Please check!")
