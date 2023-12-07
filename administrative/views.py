from django.shortcuts import render
from.models import Student
# Create your views here.
def index(request):
    stds=Student.objects.all()
    context={
        "stds":stds
    }
    return render(request,"administrative/home.html",context)