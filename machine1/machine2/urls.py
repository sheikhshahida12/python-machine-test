"""machine1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import index,Student, student_list,student, deletstudent,updatestudent,addStudentRecords,Book_list


urlpatterns = [
    path('',index),
    path('StudentRecords',Student),
    path('list',student_list),
    path('delete-student/<str:id>',deletstudent),
    path('update-student/<str:id>',updatestudent),
    path('add-student',addStudentRecords),
    path('Book',Book_list)



]
