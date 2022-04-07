from django.db import models
from datetime import datetime,timedelta

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    book_name = models.CharField(max_length=300)
    issue_date = models.DateField(auto_now=False)
    return_date = models.DateField(auto_now=False)
    branch=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    catchoice = [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
    ]
    Book_name=models.CharField(max_length=200)
    isbn = models.IntegerField()
    author_name=models.CharField(max_length=300)
    category= models.CharField(max_length=200)
    edition=models.CharField(max_length=200)

    def __str__(self):
        return self.book_name



class IssuedBook(models.Model):
    enrollment = models.CharField(max_length=30)
    ISBN = models.IntegerField()
    issuedate = models.DateField(auto_now=True)
    publication=models.CharField(max_length=100)

    def __str__(self):
        return self.enrollment
