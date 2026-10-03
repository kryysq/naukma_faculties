from django.shortcuts import render, get_object_or_404
from .models import Department, Program, Teacher

def home_view(request):
    return render(request, 'law_faculty/home.html')

def program_list_view(request):
    programs = Program.objects.all()
    return render(request, 'law_faculty/program_list.html', {'programs': programs})

def department_list_view(request):
    departments = Department.objects.all()
    return render(request, 'law_faculty/department_list.html', {'departments': departments})
