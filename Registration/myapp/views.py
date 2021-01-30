from django.shortcuts import render
#from myapp.models import *

from django.http import HttpResponse
# Create your views here.
#from Registration.myapp.models import Registration,Login


def Index(request):
    return render(request, "index.html")

#def Register(request):
 #   return render(request, "register.html")

class Registration(object):
    pass


def Register(request):
    if request.method == 'POST':
        login = Login()
        login.Email = request.POST.get("Email")
        login.Password = request.POST.get("Password")
        login.save()
        register=Registration()
        register.Name = request.POST.get("Name")
        register.Email = request.POST.get("Email")
        register.Password = request.POST.get("Password")
        register.save()
        return render(request, "index.html")
    else:
        return render(request, "register.html")





def Login(request):
    return render(request, "login.html")

def Profile(request):
    return render(request, "profile.html")

