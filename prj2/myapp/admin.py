from django.contrib import admin
from myapp.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email','dob','gender']
    search_fields=['name','email']
    fields=['name','email','dob','gender']    
    #list_editable=['email','dob','gender']
    list_per_page=5
    list_filter=['gender']


# Register your models here.

admin.site.register(Student,StudentAdmin)
