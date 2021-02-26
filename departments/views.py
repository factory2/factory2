from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Department
from .forms import DepartmentForm

def departments(request):
    departments = Department.objects.all()
    return render(request, 'departments/departments.html', {'departments': departments})

def department_detail(request, slug):
    department = get_object_or_404(Department, slug=slug)
    return render(request, 'departments/department_detail.html', {'department': department})

def department_new(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.save()
            return redirect('department_detail', slug=department.slug)
        else:
            return render(request, 'departments/department_edit.html', {'form': form})
    else:
        form = DepartmentForm()
        return render(request, 'departments/department_edit.html', {'form': form})

def department_edit(request, slug):
    department = get_object_or_404(Department, slug=slug)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            department = form.save(commit=False)
            department.save()
            return redirect('department_detail', slug=department.slug)
    else:
        form = DepartmentForm(instance=department)
        return render(request, 'departments/department_edit.html', {'form': form})
