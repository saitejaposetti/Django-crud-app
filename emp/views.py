from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

# Create your views here.
def allemployees(request):
    emp = Employee.objects.all()
    return render(request, "emp/allemployees.html", {"allemployees": emp})

def singleemployee(request, empid):
    employee = get_object_or_404(Employee, pk=empid)
    return render(request, "emp/singleemployee.html", {"employee": employee})

def addemployee(request):
    if request.method == "POST":
        employeeid = request.POST.get('employeeid')
        employeename = request.POST.get('employeename')
        employeeemail = request.POST.get('email')
        employeeaddress = request.POST.get('address')
        employeephone = request.POST.get('phone')

        e = Employee()
        e.employeeid = employeeid
        e.employeename = employeename
        e.email = employeeemail
        e.address = employeeaddress
        e.phone = employeephone
        e.save()

        return redirect("allemployees")  # Use the name of the URL pattern

    return render(request, "emp/addemployee.html")

def deleteemployee(request, empid):
    e = get_object_or_404(Employee, pk=empid)
    e.delete()
    return redirect("allemployees")

def updateemployee(request, empid):
    e = get_object_or_404(Employee, pk=empid)
    return render(request, "emp/updateemployee.html", {"singleemp": e})

def doupdateemployee(request,empid):

    updatedemployeeid = request.POST.get('employeeid')
    updatedemployeename = request.POST.get('employeename')
    updatedemployeeemail = request.POST.get('email')
    updatedemployeeaddress = request.POST.get('address')
    updatedemployeephone = request.POST.get('phone')

    emp = Employee.objects.get(pk = empid)
    emp.employeeid = updatedemployeeid
    emp.employeename = updatedemployeename
    emp.email = updatedemployeeemail
    emp.address = updatedemployeeaddress
    emp.phone = updatedemployeephone
    emp.save()

    return redirect("allemployees")
