from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages
from .models import *
from .forms import *
from django.core.mail import send_mail
from Healthify import settings
import requests

# Create your views here.
def index(request):
    user = request.session.get('user')
    return render(request,'index.html',{'user':user})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to a success page
    else:
        form = RegisterForm()
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['Email']
        password=request.POST['Password']
        
        user = Register_Form.objects.filter(Email=email,Password=password)
        uid = Register_Form.objects.get(Email=email)
        if user: #true
            print('Login Successfuly!')
            request.session["user"]=email #session create
            request.session["uid"]=uid.id
            return redirect('index')
        else:
            print('Error!')
    return render(request,'login.html')

def forgot(request):
    return render(request,'forgot.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def profile(request):
    user = request.session.get('user')
    uid = request.session.get('uid')
    cid=Register_Form.objects.get(id=uid)
    if request.method=='POST':
        update = UpdateProfile(request.POST)
        if update.is_valid():
            update=UpdateProfile(request.POST,instance=cid)
            update.save()
            print('Your Profile has been Updated')
            return redirect('index')
        else:
            print(update.errors)
    return render(request,'profile.html',{'user':user,'uid':Register_Form.objects.get(id=uid)})

def about(request):
    user = request.session.get('user')
    return render(request,'about.html',{'user':user})

def opd(request):
    user = request.session.get('user')
    return render(request,'opd.html',{'user':user})

def diagnostic(request):
    user = request.session.get('user')
    return render(request,'diagnostic.html',{'user':user})

def cardiology(request):
    user = request.session.get('user')
    return render(request,'cardiology.html',{'user':user})

def neurology(request):
    user = request.session.get('user')
    return render(request,'neurology.html',{'user':user})

def orthopadics(request):
    user = request.session.get('user')
    return render(request,'orthopadics.html',{'user':user})

def appointement(request):
    user = request.session.get('user')
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Email Send
            Date = [request.POST['Date']]
            sub = "Book Our Appointment"
            msg = f"Dear User!\nThis Mail is For HealthiFy Hospital Team,\nThe HealthiFy Hospetal Your Appointment {Date} is SuccessFull Booked\nYou Make Sour to Comming on time To Appointment.\nany query to contact on\nhealthify0989@gmail.com\nparth: 6354287550"
            from_email = settings.EMAIL_HOST_USER
            # to_email = ["pp7810559@gmail.com"]
            to_email = [request.POST['Email']]
            
            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
            
            # SMS Sending
            mobile = request.POST['Mobile']
            url = "https://www.fast2sms.com/dev/bulkV2"

            querystring = {"authorization":"gWMAeKq0ExoPnDvUiHGbj1OJsF9aC8yB7dR6L254hVcXrfNmQTc1NKT34eJrdkRYMFqlHwSsLAfmCZ70","message":f"Dear User,\nThe HealthiFy Hospital your Appointment {Date} Booked SuccessFuly!\nMake Sour Your are Coming on time.","language":"english","route":"q","numbers":f"{mobile}"}

            headers = {
                'cache-control': "no-cache"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)
            return redirect('index')  # redirect to a list view of appointments
    else:
        form = AppointmentForm()
        
   
    return render(request,'appointement.html',{'user':user})

def tipes(request):
    user = request.session.get('user')
    return render(request,'tipes.html',{'user':user})

def service24(request):
    user = request.session.get('user')
    return render(request,'service24.html',{'user':user})

def contact(request):
    user = request.session.get('user')
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # redirect to a success page
    else:
        form = ContactUsForm()
    return render(request,'contact.html',{'user':user})

def advanceOT(request):
    user = request.session.get('user')
    return render(request,'advanceOT.html',{'user':user})

def x_ray(request):
    user = request.session.get('user')
    return render(request,'x-ray.html',{'user':user})

def pharmacy(request):
    user = request.session.get('user')
    return render(request,'pharmacy.html',{'user':user})


def lab(request):
    user = request.session.get('user')
    return render(request,'lab.html',{'user':user})

def rooms(request):
    user = request.session.get('user')
    return render(request,'rooms.html',{'user':user})

def ward(request):
    user = request.session.get('user')
    return render(request,'ward.html',{'user':user})

def dashboard(request):
    if request.method=='POST':
        username=request.POST['UserName']
        password=request.POST['Password']
        
        Doctor = AdminLogin.objects.filter(UserName=username,Password=password)
        Did = AdminLogin.objects.get(UserName=username)
        if Doctor: #true
            print('Login Successfuly!')
            request.session["Doctor"]= username #session create
            request.session["Did"]=Did.id
            return redirect('appointmentdata')
        else:
            print('Error!')
    return render(request,'dashboard.html')

def appointmentdata(request):
    Doctor = request.session.get('Doctor')
    data = Appointment.objects.all()
    return render(request,'appointmentdata.html',{'Doctor':Doctor,'data':data})

def update(request,id):
    Doctor = request.session.get('Doctor')
    data = Appointment.objects.all()
    cid = Appointment.objects.get(id=id)
    if request.method=='POST':
        UpdateAppointment=AppointmentForm(request.POST)
        if UpdateAppointment.is_valid():
            UpdateAppointment=AppointmentForm(request.POST,instance=cid)
            UpdateAppointment.save()
            # Email Send
            Date = [request.POST['Date']]
            Name = [request.POST['Name']]
            sub = "Book Our Appointment"
            msg = f"Dear User!\nHello Dear'{Name}\nThe HealthiFy Hospetal Your Appointment {Date} is Changed\n Decose HealthiFy Hospital Dector is Not A avalible for this Data \nYou Make Sour to Comming on time To Appointment.\nany query to contact on\nhealthify0989@gmail.com\nparth: 6354287550"
            from_email = settings.EMAIL_HOST_USER
            # to_email = ["pp7810559@gmail.com"]
            to_email = [request.POST['Email']]
            
            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
            
            # SMS Sending
            mobile = request.POST['Mobile']
            url = "https://www.fast2sms.com/dev/bulkV2"

            querystring = {"authorization":"gWMAeKq0ExoPnDvUiHGbj1OJsF9aC8yB7dR6L254hVcXrfNmQTc1NKT34eJrdkRYMFqlHwSsLAfmCZ70","message":f"Dear User, {Name}\nThe HealthiFy Hospital your Appointment {Date} is Chagend\n \n Decose HealthiFy Hospital Dector is Not A avalible for this Data \nMake Sour Your are Coming on time.","language":"english","route":"q","numbers":f"{mobile}"}

            headers = {
                'cache-control': "no-cache"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)
            
            return redirect('appointmentdata')
        else:
            print(UpdateAppointment.errors)
    return render(request,'update.html',{'Doctor':Doctor,'data':data,'client':Appointment.objects.get(id=id)})

def deletedata(request,id):
    cid = Appointment.objects.get(id=id)
    Appointment.delete(cid)
    return redirect('appointmentdata')

def viewuser(request):
    Doctor = request.session.get('Doctor')
    data = Register_Form.objects.all()
    return render(request,'viewuser.html',{'Doctor':Doctor,'data':data})

def deleteuser(request,id):
    cid = Register_Form.objects.get(id=id)
    Register_Form.delete(cid)
    return redirect('viewuser')

def addadmin(request):
    Doctor = request.session.get('Doctor')
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointmentdata')  # redirect to admin list page
    else:
        form = AdminLoginForm()
    return render(request,'addadmin.html',{'Doctor':Doctor})

def changepass(request):
    return render(request,'changepass.html')