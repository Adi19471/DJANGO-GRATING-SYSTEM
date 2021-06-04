from django.shortcuts import render,redirect

from django.http import HttpResponse

from .forms import UserReg,Uppro,imagepro

from django.contrib.auth.decorators import login_required

# import MAIL LIBRARY 
from django.core.mail import send_mail  

from APSSDC9.settings import EMAIL_HOST_USER

# Create your views here.
def home(request):
    return render(request, 'skills/home.html')

def about(request):
    return render(request, 'skills/about.html')

def contact(request):
    return render(request, 'skills/contact.html')

def journy(request):
    return render(request, 'skills/journy.html')

# already i mentioned in urls first to Urls ->view then now no needsto view becase
# login authentication import to settings
# def login(request):
#     return render(request, 'skills/login.html')

def register(request):
    if request.method=='POST':
        to = request.POST['email']
        message = "Dear "+request.POST['username']+"You have Login VSU COLLEGE GRATING MANAGEMENT SITE" + "For refernce Your Password is :" +"Your User Id is "+request.POST['username'] +"and"+request.POST['password1']
        subject = "Reg:User Detailes from VSU SITE"
        form = UserReg(request.POST)
        if form.is_valid():
            form.save()
            send_mail(subject, message,EMAIL_HOST_USER ,[to] )
            return redirect('login')
    form = UserReg()

    return render(request,'skills/register.html',{'form':form})

@login_required
def dashbord(request):
    return render(request, 'skills/dashbord.html')


def logout(request):
    return render (request,'skills/logout.html')

def profile(request):
    return render(request,'skills/profile.html')

@login_required
def up(request):
    if request.method == "POST":
        t = Uppro(request.POST,instance = request.user)
        y = imagepro(request.POST,request.FILES,instance=request.user.update)

        if t.is_valid() and y.is_valid():
            t.save()
            y.save()
            return redirect('profile')
    t = Uppro(instance=request.user)
    y = imagepro(instance=request.user.update)
    return render(request, 'skills/uppro.html',{'t':t,'y':y})


def mail(request):
    if request.method == "POST":
       to = request.POST['email']
       cc = request.POST['title']
    #    body_ts =request.POST['body_ts']

       mes = request.POST['message']
     
       email = send_mail(cc,mes,EMAIL_HOST_USER,[to])
       

    return render(request,'skills/mail.html')


    