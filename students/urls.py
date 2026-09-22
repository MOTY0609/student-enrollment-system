from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name=('home_page')),
    path('home/sign_up/', views.sign_up, name=('sign_up')),
    path('registered_students', views.student_list, name=('student_list')),
    path('register/', views.register_student, name=('register_student')),
    path('<int:pk>/edit_student', views.edit_student, name=('edit_student')),
    path('<int:pk>/delete_student', views.delete_student,
         name=('delete_student')),
    path('home/welcome', views.student_home_page, name=('student_home_page'))
]
