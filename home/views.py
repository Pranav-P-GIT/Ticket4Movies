from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Film,Seat


# Create your views here.
def thankyou(request):
    id=request.GET["id"]
    if request.method=="POST":
        ticket=request.POST["q"]
        data=Film.objects.filter(id=id)
        seat=Seat.objects.get(id=id)
        t1=int(seat.available)-int(ticket)
        Seat.objects.filter(id=id).update(available=t1)
        price=int(seat.price)*int(ticket)
    return render(request,"ticketpage.html",{"data":data,"ticket":ticket,"price":price})


def login(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["psw"]
        check=auth.authenticate(username=username,password=password)
        if check is not None:
            auth.login(request,check)
            return redirect("/")
        else:
            msg="INVALID USERNAME OR PASSWORD"
            return render(request,"loginpage.html",{"msg":msg})
    else:
        return render(request,"loginpage.html")
    
    
def logout(request):
    auth.logout(request)
    return redirect("/")



def register(request):
    if request.method=="POST":
        username=request.POST["uname"]
        email=request.POST["email"]
        password=request.POST["psw"]
        repassword=request.POST["psw-repeat"]
        ucheck=User.objects.filter(username=username)
        echeck=User.objects.filter(email=email)
        if ucheck:
            msg="USERNAME ALREADY EXISTS"
            return render(request,"registerpage.html",{"msg":msg})
        elif echeck:
            msg="EMAIL ALREADY EXITS"
            return render(request,"registerpage.html",{"msg":msg})
        elif password=="" or password!=repassword:
            msg="RE-PASSWORD ERROR"
            return render(request,"registerpage.html",{"msg":msg})
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save();
            return redirect("/")
    else:
        return render(request,"registerpage.html")


def movie(request):
    id=request.GET["id"]
    data=Film.objects.filter(id=id)
    seat=Seat.objects.filter(id=id)
    return render(request,"moviepage.html",{"data":data,"seat":seat})


def index (request):
    data= Film.objects.all()
    seat= Seat.objects.all()
    
        
    return render(request,"indexpage.html",{"data":data,"seat":seat})

def gallery(request):
    return render(request,"gallery.html")


def booking (request):
    id=request.GET["id"]
    if request.method == "POST":
        seat=Seat.objects.filter(id=id)
        data=Film.objects.get(id=id)
    return render(request,"booking.html",{"seat":seat,"data":data})