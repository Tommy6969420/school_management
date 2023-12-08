from django.shortcuts import render
from.models import Student,Class
from django.http import Http404
from.forms import StudentForm
# Create your views here.
def studentsinfo(request):
    stds=Student.objects.all()
    context={
        "stds":stds
    }
    return render(request,"administrative/students.html",context)
def classesinfo(request):
    classes=Class.objects.all()
    subjects=Class.objects.values_list("subject",flat=True)  
    context={
        "classes":classes,
        "subjects":subjects,
    }
    return render(request,"administrative/classes.html",context)
def studentfilter(request,id):
    try:
        std=Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404
    context={
        "std":std
    }
    return render(request,"administrative/students_id.html",context)
def admission_form(request):
    
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form=StudentForm()
            context={
                "form":form,
                "sucess":"Admission Submit Sucess"
            }
            return render(request,"administrative/admission.html",context)
    form=StudentForm()
    context={
            "form":form,
        }
    return render(request,"administrative/admission.html",context)