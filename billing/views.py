from django.shortcuts import render
from administrative.models import Student
from.models import ClassBills,Billing,TransportRoutes
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
    # due_obj=Billing.objects.filter(student_id=student_id).order_by("-recipt_no")
    # prev_due=due_obj.order_by("-recipt_no").values("recipt_no","due","date_of_billing")[:1]
    due_obj=Billing.objects.filter(student_id=student_id).order_by("-recipt_no")
    prev_due=due_obj.order_by("-recipt_no").values("recipt_no","due","date_of_billing")[:1]
    for item in prev_due:
            receipt_number = item['recipt_no']
            due_amount = item['due']
            billing_date = item['date_of_billing']
    
        
    
    try:
        payload={
                "name":obj.std_name,
                "class":obj.std_class.class_name,
                "admission_fee":class_obj.admissioin_fee,
                "monthly_fee":class_obj.monthly_fee,
                "recipt_no":receipt_number,
                "due_amount":due_amount,
                "billing_date":billing_date,
                  
                }
    except UnboundLocalError :
        receipt_number=0
        due_amount=0
        billing_date=0
        payload={
                "name":obj.std_name,
                "class":obj.std_class.class_name,
                "admission_fee":class_obj.admissioin_fee,
                "monthly_fee":class_obj.monthly_fee,
                "recipt_no":receipt_number,
                "due_amount":due_amount,
                "billing_date":billing_date,                  
                }                                   
    return JsonResponse({                                                                                                                   
            'status':True,
            "payload":payload,
        })
def billing(request):
    if request.method=="POST":
        form=BillingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BillingForm()
            context={
                "form":form,
                }
            return render(request,"billing/billing.html",context)
    transport=TransportRoutes.objects.all()
    form=BillingForm()
    context={
         'form':form,
         "transport":transport
    }
    return render(request,"billing/billing.html",context)
