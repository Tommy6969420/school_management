from django.shortcuts import render
from administrative.models import Student
from django.http import Http404
# Create your views here.
def billing(request):
    if request.method=="POST":
        std_name=request.POST.get("name")
        if std_name==True:
            try:
                std=Student.objects.all().filter(std_name=std_name)
                context={
                "stds":std,   
                }
                return render(request,"billing/billing.html",context)
            except Student.DoesNotExist:
                
                context={
                    "std_query":std_name+" Doesnot Exist",
                }
                return render(request,"billing/billing.html",context)
        std_class=request.POST.get("class")
        if std_class==True:
            try:
                std=Student.objects.all().filter(std_class=std_class)
                context={
                "stds":std,   
                }
                return render(request,"billing/billing.html",context)
            except Student.DoesNotExist:
                
                context={
                    "std_query":std_name+" Doesnot Exist",
                }
                return render(request,"billing/billing.html",context)
    return render(request,"billing/billing.html")
