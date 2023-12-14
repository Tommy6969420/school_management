from django.shortcuts import render
from administrative.models import Class, Student
from billing.models import ClassBills, Billing,TransportRoutes
def home(request):
    classes_count=Class.objects.count()
    std_no=Student.objects.count()
    class_bills=ClassBills.objects.all()
    billings=Billing.objects.count()
    transp_routes=TransportRoutes.objects.all()
    print(class_bills)
    context={

        "classes_list":classes_count,
        "std_no":std_no,
        "class_bills":class_bills,
        "billings":billings,
        "transp_routes":transp_routes


    }
    return render(request,"home.html",context)
