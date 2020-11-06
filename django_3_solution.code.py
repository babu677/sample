





#Todo Django

# to create project
'''
django-admin.py startproject company
'''
# to create app
# come back to Project Dir with cd
'''
python3 manage.py startapp staff
'''



#2. ORM

from django.db import models

class Employee_table(models.Model):
    Emp_name = models.CharField('Employee Name', max_length=120)
    Department = models.CharField('Department ', max_length=120)
    Email = models.EmailField(max_length = 254)
    Date_of_birth = models.DateTimeField('Event Date')
    Picture = models.ImageField(upload_to ='imgs/') # # file will be saved to MEDIA_ROOT / imgs

def __str__(self):
        return self.Emp_name




class Department_table(models.Model):
    Emp_name=models.Foreignkey(Employee_table)
    Department_name = models.CharField('Department name', max_length=120)
   
def __str__(self):
        return self.Department_name



#3 admin.py

from django.contrib import admin
from .models import Employee_table, Department_table
# Register your models here.

class AdminEmployee_table(admin.ModelAdmin):
    list_display=['Emp_name','Department','Email','Date_of_birth','Picture']

class AdminDepartment_table(admin.ModelAdmin):
    list_display=['Department']

  

admin.site.register(Employee_table,AdminEmployee_table)
admin.site.register(Department_table,AdminDepartment_table)

#4 commands

run manage.py
makemigration
migrate
and
runserver




# 5 views.py  #7
'''
django-admin check auth admin myapp
'''
from django.shortcuts import render
from django.views import generic
from genericviews.forms import Emp_form,Department_form
import datetime as dt
from django.template.loader import get_template
from django.http.response import HttpResponse
from genericviews.models import Employee_table,Department_table



def emp(request):
    if request.method=="POST":
        form=Empform{request.POST}
        if .form.is_valid():
            Emp_name=request.POST.get('Emp_name',")
            Department=request.POST.get('Department',")
            Email=request.POST.get('Email',")
            Date_of_birth=request.POST.get('Date_of_birth',")
            Picture =request.POST.get('Picture ',")

         
         Employee_table=Employee_table(Emp_name=Emp_name,Department=Department,Email=Email,Date_of_birth=Date_of_birth,Picture=Picture,)
         Employee_table.save()                             
            
        form=Emp_form()
        return render(request,'genericviews/emp.Html',{'form':form})
                                      
    else:
        form=Emp_form()
        return render(request,'genericviews/emp.Html',{'form':form}))


    
''' Here u go with template files name for views.py (employee)'''
# 7


  
class IndexView(generic.ListView):
    context_object_name='list'
    template_name='genericviews/index.Html'




    def get_queryset(self):
        return emp.objects.all()

class Detailsview(generic.Detailsview):
    Model=Emp
    template_name='genericviews/Detail.Html'
    
# 8
''' Here u go with template files name for views.py (department)'''


class IndexdeptView(generic.ListView):
    context_object_name='list'
    template_name='genericviews/ dmt.Html'




    def get_queryset(self):
        return Department.objects.all()

class Detailsview(generic.Detailsview):
    Model=department
    template_name='genericviews/dept.Html'




#6.forms.py

forms.py

from django import forms

class EmpForm(forms.Form):
    Employee_name=forms.CharField(
        label='Enter Your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'name here...'
            }
        )
    )
    Department = forms.CharField(
        label='Enter Your department Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'father name here...'
            }
        )
    )
    Date_of_birth= forms.datetimefield(
        label='Enter Your date-of-birth',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter your mother name'
            }
        )

    )
    picture = forms.image_field(
        label='Enter Your picture',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter your mobile number'
            }
        )

    )
    EmailId = forms.EmailField(
        label='Enter Your EmailId',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter your emailid'
            }
        )

    )


 Class DepartmentForm(form.Forms):

    Department = forms.CharField(
        label='Enter Your department_name,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter your salary here...'
            }
        )

    )
