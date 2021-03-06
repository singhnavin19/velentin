from .models import Optionelect
from django.shortcuts import render,HttpResponse

# Create your views here.
def homePage(request):
    return render(request,"homePage.html");

def helloPage(request):
    return render(request, "HelloPage.html")

def AddTwoNosPage(request):
    optselect=Optionelect()
    optselect.no1=0
    optselect.no2=0
    optselect.opt=["Add","Subtract","Division"]
    return render(request,"AddTwoNosPage.html")

def additionTwoNos(request):
    val1=int(request.GET["no1"])
    val2=int(request.GET["no2"])
    val3=int(request.GET["opt"])
    result=0
    if val3==1:
        result=val1+val2
    else:
        result=val1-val2
    # val1=int(request.POST["no1"])
    # val2=int(request.POST["no2"])
    return render (request,"AddTwoNosPage.html",{'result':result})