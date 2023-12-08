from django.db import models
from administrative.models import Class,Student
from django.utils import timezone
# Create your models here.
class ClassBills(models.Model):
    indv_class= models.OneToOneField(Class,on_delete=models.CASCADE)
    monthly_fee=models.IntegerField()
    admissioin_fee=models.IntegerField()
    T_C_certificate_fee=models.IntegerField()

class IndividualStudentFee(models.Model):
    class_wise=models.ForeignKey(ClassBills, on_delete=models.CASCADE)
    transportation=models.IntegerField(default=0)

class Billing(models.Model):
    student_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    recipt_no=models.AutoField(primary_key=True,unique=True,)
    date_of_billing=models.DateField(default=timezone.now)
    #all three of fields below require default values to workon 
    total=models.IntegerField()
    paid=models.IntegerField()
    due=models.IntegerField()
    previous_due=models.IntegerField()
