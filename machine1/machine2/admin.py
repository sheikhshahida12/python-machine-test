from django.contrib import admin
from .models import Book,student,IssuedBook

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class StudentRecordsAdmin(admin.ModelAdmin):
    pass
admin.site.register(student, StudentRecordsAdmin)


class IssuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IssuedBookAdmin)
