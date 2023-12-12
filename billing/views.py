from django.shortcuts import render
from administrative.models import Student
from.models import ClassBills
from django.http import Http404,JsonResponse, HttpResponse
from.forms import BillingForm,ClassBillsForm
# Create your views here.
def search_filter(request):

    if request.method=="POST":
        std_name=request.POST.get("name")
        if std_name==True:
            try:
                std=Student.objects.all().filter(name__startswith=std_name)
                context={
                "stds":std,   
                }
                return render(request,"billing/search_filter.html",context)
            except Student.DoesNotExist:
                
                context={
                    "std_query":std_name+" Doesnot Exist",
                }
                return render(request,"billing/search_filter.html",context)
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
    return render(request,"billing/search_filter.html")
def get_student_info(request):
    student_id=request.GET.get("student_id")
        # print(str(student_id))
    obj=Student.objects.get(id=student_id)
    class_obj=ClassBills.objects.get(indv_class_id=obj.std_class.id)
    print(class_obj.admissioin_fee)
    payload={
                "name":obj.std_name,
                "class":obj.std_class.class_name,
                "admission_fee":class_obj.admissioin_fee,
                "monthly_fee":class_obj.monthly_fee,
                }
    return JsonResponse({
            'status':True,
            "payload":payload,
        })
def billing(request):
    if request.method=="POST":
        class_bills=ClassBills.objects.all()
        form=BillingForm()
        if form.is_valid():
            form.save()
            form=BillingForm()
            context={
                "form":form,
                "class_bills":class_bills,
                "success":"Billing Sucess"
            }
            return render(request,"billing/billing.html",context)
    form=BillingForm()
    class_bills=ClassBills.objects.all()
    context={
         'form':form,
         "class_bills":class_bills,
    }
    return render(request,"billing/billing.html",context)
