from django.db import models
from administrative.models import Class,Student
from django.utils import timezone
# Create your models here.
class TransportRoutes(models.Model):
    route=models.CharField(max_length=64,blank=False,null=False,unique=True)
    transport_fee=models.IntegerField(blank=False,null=True,default=0)
    def __str__(self):
        return f"{self.transport_fee}"
class ClassBills(models.Model):
    indv_class= models.ForeignKey(Class,on_delete=models.CASCADE,)
    admissioin_fee=models.IntegerField(default=0,blank=True,null=True)
    monthly_fee=models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return f"{self.indv_class},{self.monthly_fee},{self.admissioin_fee}"
class Months(models.Model):
    MONTHS_CHOICES=[
     ("Baisakh","Baisakh"),
     ("Jestha","Jestha"),
     ("Ashad","Ashad"),
     ("Shrawan","Shrawan"),
     ("Bhadra","Bhadra"),
     ("Ashoj","Ashoj"),
     ("Kartik","Kartik"),
     ("Mangsir","Mangsir"),
     ("Paush","Paush"),
     ("Magh","Magh"),
     ("Falgun","Falgun"),
     ("Chaitra","Chaitra"),

]
    name=models.CharField(choices=MONTHS_CHOICES,max_length=64,unique=True)
    def __str__(self):
        return f"{self.name}"
class Billing(models.Model):
    recipt_no=models.AutoField(primary_key=True,unique=True,)
    date_of_billing=models.DateField(default=timezone.now)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,)
    admission=models.IntegerField(null=True,blank=True,default=0,) 
    monthly=models.IntegerField(null=True,blank=True,default=0,)
    months=models.ManyToManyField(Months,blank=False,)
    transportation=models.ForeignKey(TransportRoutes,blank=False,null=True,on_delete=models.CASCADE,default=False)
    T_C_certificate_fee=models.IntegerField(default=0,blank=True,null=True)
    others=models.IntegerField(default=0,blank=True,null=True)
    previous_due=models.IntegerField(null=True,blank=True,default=0)
        #all three of fields below require default values to workon 
    total=models.IntegerField(null=False,blank=False,default=0)
    paid=models.IntegerField(null=False,blank=False,default=0)
    due=models.IntegerField(null=True,blank=True,default=0,)    
    def __str__(self):
        return f"{self.recipt_no},{self.student},{self.due},{self.previous_due}"
    # class Meta:
    #     # Define unique constraint for student and month
    #     unique_together = ('student', 'months')