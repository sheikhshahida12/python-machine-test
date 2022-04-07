from django.forms import ModelForm
from .models import student,Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForms(ModelForm):
    class Meta:
        model=student
        fields='__all__'


class AdminForms(UserCreationForm):
        class Meta:
            model = User
            fields = ['username','email','password']



class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

