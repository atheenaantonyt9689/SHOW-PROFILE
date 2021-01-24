from django.shortcuts import render
#from myapp.models import Register,Login
from django.http import HttpResponse
# Create your views here.
def Index(request):
    return render(request, "index.html")

#def Register(request):
 #   return render(request, "register.html")

def Register(request):
    if request.method == 'POST':
        login = Login()
        login.userid = request.POST.get("Name")
        login.password = request.POST.get("Password")
        login.save()
        return render(request, "index.html")
    else:
        return render(request, "register.html")





def Login(request):
    return render(request, "login.html")

def Profile(request):
    return render(request, "profile.html")

