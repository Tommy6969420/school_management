from django.shortcuts import render
from.models import Student,Class
from django.http import Http404
from.forms import StudentForm,ClassForm,SubjectForm
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
           # roll_no=str(form["roll_no"].value())
            # if roll_no 
            form.save()
            form=StudentForm()
            context={
                "form":form,
                "sucess":"Admission Submit Sucess"
            }
            return render(request,"administrative/admission.html",context)
    # roll_no=Student.objects.values("roll_no").order_by("-roll_no")[:1]

    # for item in roll_no:
    #     roll=item["roll_no"]
    form=StudentForm()
    context={
            "form":form,
            # "def_roll":roll,
        }
    
    return render(request,"administrative/admission.html",context)
def subject_add(request):
    form_subject=SubjectForm(request.POST)
    if form_subject.is_valid():
        form_subject.save()
        form_subject=SubjectForm()
        context={
                "form_subject":form_subject,
                "sucess":"Submit Sucess"
            }
        return render(request,"administrative/class_subject_add.html",context)
    form_subject=SubjectForm()
    context={
                "form_subject":form_subject,
                "unsucess":"Unsucessfull",
        }
    return render(request,"administrative/class_subject_add.html",context)
def class_add(request):
    if request.method=='POST':
        form_class=ClassForm(request.POST)
        if form_class.is_valid():
            form_class.save()
            form_class=ClassForm()
            context={
                "form_class":form_class,
                "sucess":"Submit Sucess"
            }
            return render(request,"administrative/class_subject_add.html",context)
    form_class=ClassForm()
    context={
                "form_class":form_class,
                # "form_subject":form_subject,
                "unsucess":"Unsucessfull",
        }
    return render(request,"administrative/class_subject_add.html",context)