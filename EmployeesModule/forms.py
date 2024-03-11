
from django import forms
from EmployeesModule.models import EmployeeForm
from EmployeesModule.models import Registration
from EmployeesModule.models import employee_Next_of_Kin


class Employees(forms.ModelForm):
    class Meta:
        model = EmployeeForm
        fields = ['full_name', 'email', 'emp_code', 'mobile_no','position']


class Employee_list(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'phone_no', 'password']





class employee_Next_of_KinForm(forms.ModelForm):
    class Meta:
        model = employee_Next_of_Kin
        fields = ['full_name', 'employee', 'ID_number', 'phone_no']



