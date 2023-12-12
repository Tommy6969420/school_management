from django.db import models
from administrative.models import Class,Student
from django.utils import timezone
# Create your models here.
class TransportRoutes(models.Model):
    route=models.CharField(max_length=64,blank=False,null=False)
    transport_fee=models.IntegerField(blank=False,null=False)
    def __str__(self):
        return f"Route: {self.route} Transport Fee:{self.transport_fee}"
class ClassBills(models.Model):
    indv_class= models.ForeignKey(Class,on_delete=models.CASCADE,)
    admissioin_fee=models.IntegerField(default=0,blank=True,null=True)
    monthly_fee=models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return f"{self.indv_class},{self.monthly_fee},{self.admissioin_fee}"
class Billing(models.Model):
    recipt_no=models.AutoField(primary_key=True,unique=True,)
    date_of_billing=models.DateField(default=timezone.now)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=False)
    transportation=models.ForeignKey(TransportRoutes,blank=True,null=True,on_delete=models.CASCADE)
    T_C_certificate_fee=models.IntegerField(default=0,blank=True,null=True)
    others=models.IntegerField(default=0,blank=True,null=True)
        #all three of fields below require default values to workon 
    total=models.IntegerField(null=True,blank=True,default=0)
    paid=models.IntegerField(null=True,blank=True,default=0)
    due=models.IntegerField(null=True,blank=True,default=0)
    previous_due=models.IntegerField(null=True,blank=True,default=0)
    def __str__(self):
        return f"{self.student.std_name} {self.student.std_class.class_name} "

