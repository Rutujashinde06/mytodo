# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from eapp.models import Employeetask
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth  import authenticate,login
from eapp.forms import User,UserForm

# Create your views here.


def index(request):
    v=Employeetask.objects.all()
    content={}
    content['tasks']=v
    return render(request,'index.html',content)

def registration(request):
     content={}
     regobj=UserForm()
     print(regobj)
     content['userform']=regobj
     if request.method=="POST":
           regobj=UserForm(request.POST)
         #  print(regobj)
         #  print(regobj.is_valid())
           if regobj.is_valid():
            regobj.save()
            content['success']="User Created Successfully"
           return render(request,'registration.html',content)
     else:
        return render(request,'registration.html',content)      

     



     
     

def login(request):
     if request.method=="POST":
           dataobj=AuthenticationForm(request=request,data=request.POST)
           #print(dataobj)
           if dataobj.is_valid():
                uname=dataobj.cleaned_data['username']
                upass=dataobj.cleaned_data['password']
                #print(uname)
                #print(upass)
                u=authenticate(username=uname,password=upass)
                #print(u)
                if u:
                     login(request,u)
                     return redirect('/')
     else:
          obj=AuthenticationForm()
          content={}
          content['loginform']=obj
          return render(request,'login.html',content)     



def addtask(request):
    if request.method== "POST":
        n=request.POST['name']
        c=request.POST['cat']
        s=request.POST['status']
        p=Employeetask.objects.create(name=n,cat=c,status=s)
        p.save()
        data=Employeetask.objects.all()
        content={}
        content['tasks']=data
        return render(request,'addtask.html',content)
    else:    
       # print("In else part")
        p=Employeetask.objects.all()
        content={}
        content['tasks']=p
        return render(request,'addtask.html',content)



def edittask(request,rid):
    print('Task to be edited:',rid)
    
    if request.method=="POST":
        tname=request.POST['name']
        cat=request.POST['cat']
        status=request.POST['status']

        print(tname)
        print(cat)
        print(status)
        p=Employeetask.objects.filter(id=rid)
        p.update(name=tname,cat=cat,status=status)
        return redirect('/addtask')


    else:
        p=Employeetask.objects.filter(id=rid)
        content={}
        content['tasks']=p
        return render(request,'edittask.html',content)


def deltask(request,rid): 
   # print('Id to be deleted:',rid) 
   p=Employeetask.objects.filter(id=rid)
   p.delete()
   return redirect('/addtask')

def catfilter(request,sid):
    
    q2=Q(cat=sid)
    data=Employeetask.objects.filter(q2)
    content={}
    content['tasks']=data
    return render(request,'index.html',content)

def sort(request,sv):
    q1=Q(status=sv)
    data=Employeetask.objects.filter(q1)
    content={}
    content['tasks']=data
    return render(request,'index.html',content)