from django.shortcuts import render

from django.http import HttpResponse  


# Create your views here.
"""def index(request):
	#return HttpResponse("<h2>welcome to all!!!!</h2>") 
	return render(request,'index.html') 

def registration(request):
	return render(request,'registration.html') 

	  

def login(request):
   return render(request,'login.html') 

def welcome(request):
   val=request.GET.get("text",'default')
   print(val)
   return render(request,'welcome.html') 


from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm"""

#from first.forms import StudentForm  
from first.models import Student  
#Create your views here. 
def index(request):
	#return HttpResponse("<h2>welcome to all!!!!</h2>") 
	return render(request,'index.html')

def new(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'new.html',{'form':form})
    

def show(request):  
    student = Student.objects.all()  
    return render(request,"show.html",{'student':student}) 

def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'edit.html', {'student':student}) 


def update(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'student': student}) 

def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/show") 
