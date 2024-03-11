from django.db import models

class EmployeeForm(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    emp_code = models.CharField(max_length=5)
    mobile_no = models.CharField(max_length=10)
    position = models.CharField(max_length=10)
    def __str__(self):
        return self.full_name
#
class Registration(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     phone_no = models.IntegerField(max_length=10)
     password = models.CharField(max_length=10)


class employee_Next_of_Kin(models.Model):
     full_name = models.CharField(max_length=50)
     employee = models.CharField(max_length=50)
     ID_number = models.IntegerField(max_length=9)
     phone_no = models.CharField(max_length=10)