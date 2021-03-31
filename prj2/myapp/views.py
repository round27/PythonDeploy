from django.shortcuts import render, redirect
from myapp.models import Student
from myapp.forms import StudentForm,EmailForm
from django.core.paginator import Paginator
from django.contrib import messages

from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def home(request):
    return render (request,'home.html',{'title':'Home'})

def index(request):
    std=Student.objects.order_by('-id')
    paginator=Paginator(std,15)
    page=request.GET.get('page')
    students=paginator.get_page(page)
    context={'title':'List of student','students':students}
    return render(request,'student/index.html',context)

def show(request,id):
    student=Student.objects.get(pk=id)
    form=StudentForm(request.POST or None, instance=student)
    context={'title':'Details','student':student}
    return render(request,'student/details.html',context)

def create(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request,'Data inserted successfully')
            return redirect('student:index')
    else:
        form=StudentForm()
    
    context={'title':'Create','form':form}
    return render(request,'student/create.html',context)

def edit(request,id):
    student=Student.objects.get(pk=id)
    form=StudentForm(request.POST or None, instance=student)
    context={'title':'Edit','student':student,'form':form}
    return render(request,'student/edit.html',context)


def update(request,id):
    student=Student.objects.get(pk=id)
    form=StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        print(form)
        form.save()
        messages.info(request,'Data updated successfully')        
        return redirect('student:index')
    else:
        print('Data not valid')
    context={'title':'Edit','form':form}
    return render(request,'student/edit.html',context)

def delete(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    messages.add_message(request,messages.SUCCESS,'Data deleted successfully ')
    return redirect('student:index')


def sendEmail(request):
    if request.method=='POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            sub=form.cleaned_data['subject']
            mes=form.cleaned_data['message']
            email=form.cleaned_data['email']
            try:
                mail=EmailMessage(sub,mes,settings.EMAIL_HOST_USER,[email])
                if request.FILES:
                    files=request.FILES.getlist('attach')
                    for f in files:
                        mail.attach(f.name,f.read(),f.content_type)
                mail.send()
                messages.success(request,'Email sent successfully')
                return redirect('student:index')
            except:
                messages.error(request,'Email not sent successfully')
    else:
        form=EmailForm()
    
    context={'title':'Email','form':form}


    return render(request,'email_form.html',context)