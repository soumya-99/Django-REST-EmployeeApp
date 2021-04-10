from django.shortcuts import render
# We can use it (csrf_exempt) to allow other domains to easily access our API methods
from django.views.decorators.csrf import csrf_exempt
# By other domains, our front-end project, we also need something called JSONParser to parse the incomming data into the data model
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Department, Employees
from .serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def departmentAPI(request, id=0):
    # Fetch Data
    if request.method == "GET":
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(
            departments, many=True)  # converted into JSON format
        # The parameter safe=False is basically use to inform Django that what we are trying to convert to JSON format that's actually a valid fromat to be converted and we are fine if there're any issues
        return JsonResponse(departments_serializer.data, safe=False)

    # Create Data
    elif request.method == "POST":
        department_data = JSONParser().parse(request)  # parse request as JSON
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse('Failed to add Data!!', safe=False)

    # Update Data
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        department = Department.objects.get(
            DepartmentID=department_data["DepartmentID"])
        department_serializer = DepartmentSerializer(
            department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update!!", safe=False)

    # Delete Data
    elif request.method == "DELETE":
        department = Department.objects.get(DepartmentID=id)
        department.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
    return JsonResponse("Error occurred while Deleting!!", safe=False)


@csrf_exempt
def employeeAPI(request, id=0):
    # Fetch Data
    if request.method == "GET":
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(
            employees, many=True)  # converted into JSON format
        # The parameter safe=False is basically use to inform Django that what we are trying to convert to JSON format that's actually a valid fromat to be converted and we are fine if there're any issues
        return JsonResponse(employees_serializer.data, safe=False)

    # Create Data
    elif request.method == "POST":
        employee_data = JSONParser().parse(request)  # parse request as JSON
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse('Failed to add Data!!', safe=False)

    # Update Data
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(
            EmployeeID=employee_data["EmployeeID"])
        employee_serializer = EmployeeSerializer(
            employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update!!", safe=False)

    # Delete Data
    elif request.method == "DELETE":
        employee = Employees.objects.get(EmployeeID=id)
        employee.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
    return JsonResponse("Error occurred while Deleting!!", safe=False)


@csrf_exempt
def SaveImageFile(request):
    # We are extracting the uploaded file from the request
    file = request.FILES["myFile"]
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)