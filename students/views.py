from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'students/sign_up.html', {"form": form})


def home_page(request):
    return render(request, 'students/home_page.html')


def student_home_page(request):
    return render(request, 'students/student_home_page.html')


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html',
                  {'students': students})


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/register_student.html', {'form': form})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html',
                  {'form': form, 'student': student})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/delete_student.html',
                  {'student': student})


def courses(request):
    pass
