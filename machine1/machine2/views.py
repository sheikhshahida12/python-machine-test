from django.shortcuts import render,redirect
from .forms import StudentForms,BookForm
from .models import student,Book
from .forms import AdminForms



# Create your views here.
def index(request):
    return render(request,'index.html')

def Student(request):
    form=StudentForms
    if request.method == 'POST':
        stude_form = StudentForms(request.POST)
        if stude_form.is_valid():
            stude_form.save()
            return redirect('/student')
    return render(request,'student.html',{'form':form})

def student_list(request):
    data=student.objects.all()
    return render(request,'studentlist.html',{'data':data})

def deletstudent(request,id):
    name=student.objects.get(id=id)
    name.delete()
    return redirect('/list')



def updatestudent(request,id):
    name=student.objects.get(id=id)
    form=StudentForms(instance=name)
    if request.method == 'POST':
        saveform=StudentForms(request.POST or None,instance=name)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'updatestudent.html',{'form':form})


def addStudentRecords(request):
    form=StudentForms
    if request.method == 'POST':
        saveform=StudentForms(request.POST)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'addStudentRecords.html',{'form':form})

def register(request):
    form=AdminForms
    if request.method=='POST':
        admin_form=AdminForms(request.POST)
        if admin_form.is_valid():
            admin_form.save()
            return redirect('/registeration.html',{'form':form})

    else:
        form=AdminForms

    return render(request,'registration/admin')

def book(request):
    form=BookForm
    if request.method == 'POST':
        saveform=BookForm(request.POST)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'book.html',{'form':form})

def Book_list(request):
    form=Book.objects.all()
    return render(request,'booklist.html',{'form':form})

def deletBook(request,id):
    name=Book.objects.get(id=id)
    name.delete()
    return redirect('/list')



def updateBook(request,id):
    name=Book.objects.get(id=id)
    form=BookForm(instance=name)
    if request.method == 'POST':
        saveform=BookForm(request.POST or None,instance=name)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'updatebook.html',{'form':form})


def addBookRecords(request):
    form=BookForm
    if request.method == 'POST':
        saveform=BookForm(request.POST)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'addBookRecords.html',{'form':form})

def login(request):
    form=AdminForms
    if request.method=='POST':
        admin_form=AdminForms(request.POST)
        if admin_form.is_valid():
            admin_form.save()
            return redirect('/login.html',{'form':form})

    else:
        form=AdminForms

    return render(request,'login/admin')


