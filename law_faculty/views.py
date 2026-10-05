from django.shortcuts import render, get_object_or_404
from .models import Department, Program, Teacher, Specialty

def home_view(request):
    return render(request, 'law_faculty/home.html')

def specialty_list_view(request):
    specialties = Specialty.objects.all()
    return render(request, 'law_faculty/specialties.html', {'specialties': specialties})

def program_list_view(request):
    programs = Specialty.objects.all()
    return render(request, 'law_faculty/program_list.html', {'programs': programs})

def program_detail_view(request, pk):
    program = get_object_or_404(Specialty, pk=pk)
    return render(request, 'law_faculty/program_detail.html', {'program': program})

def department_list_view(request):
    departments = Department.objects.all()
    return render(request, 'law_faculty/department_list.html', {'departments': departments})
