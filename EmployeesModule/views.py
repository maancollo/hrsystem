from django.shortcuts import render, redirect
from EmployeesModule.forms import employee_Next_of_Kin
from EmployeesModule.models import EmployeeForm
from EmployeesModule.forms import Employees
from EmployeesModule.forms import Employee_list


# Create your views here.
def employee_form(request, id=0):
    if request.method == 'GET':
        form = Employees(request.GET)
        return render(request, 'employee_form.html', {'form': form})
    else:
        form = EmployeeForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('/EmployeesModule/employee_list')


def employee_delete(request):
    employee = EmployeeForm.objects.get(pk=id)
    employee_list.delete()
    return redirect('employee/employee_list')
    # return render(request, template_name='employee_form.html')




def employee_list(request):
        form = Employee_list(request.GET)
        context = {'employee_list': EmployeeForm.objects.all()}
        return render(request, template_name='employee_list.html',context=context)


def NextOfKin(request):
    form = employee_Next_of_Kin
    return render(request, template_name='NextOfKin.html')


