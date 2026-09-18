from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
from myApp.models import Departments,Employees
from myApp.serializers import DepartmentSerializer,EmployeeSerializer
from django.core.files.storage import default_storage



# Create your views here.
@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added  Successfully",safe=False)
        return JsonResponse(str(departments_serializer.errors),safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse(str(departments_serializer.errors),safe=False)
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse(str(employees_serializer.errors),safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse(str(employees_serializer.errors),safe=False)
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)
@csrf_exempt
def SaveFile(request):
 file=request.FILES['file']
 file_name=default_storage.save(file.name,file)
 return JsonResponse(file_name,safe=False)


def welcomepage(response):
    return HttpResponse("WELCOME TO MY DJANGO PAGE!")

def welcomeformpage(response):
    pagecontent = "Welcome to my Django page!"
    data ={
        'welcome': pagecontent
    }
    return render(response, 'welcome.html', data)

def register(request):
    fname = ''
    lname = ''
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
    data = {
        'name' : str(fname) + " " + str(lname)
    }
    
    return render(request, 'register.html', data)

def calculate(a, op, b):
    if op == 'add':
        return a + b
    elif op == 'subtract':
        return a - b
    elif op == 'multiply':
        return a * b
    elif op == 'divide':
        return a / b

def mdas(request):
    result = 0
    fnum = ''
    snum = ''
    tnum = ''
    qnum = ''
    action1 = 'add'
    if request.method == 'POST':
        fnum = request.POST.get('first_number')
        snum = request.POST.get('second_number')
        tnum = request.POST.get('third_number')
        qnum = request.POST.get('fourth_number')
        action1 = request.POST.get('action1')

        result = (calculate(float(fnum), action1, float(snum)) * float(tnum)) / float(qnum)

    data = {
        'result': result,
        'first_number': fnum,
        'second_number': snum,
        'third_number': tnum,
        'fourth_number': qnum,
        'action1': action1
    }
    return render(request, 'addition.html', data)