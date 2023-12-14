from django.db import models
from django.utils import timezone

# Create your models here.
class Subject(models.Model):
    subj_name=models.CharField(max_length=64)
    def __str__(self):
        return f"{self.subj_name}"
class Class(models.Model):
    class_name=models.CharField(max_length=64,default="")
    section_choices=[
        ("Rose","Rose"),
        ("Lotus","Lotus"),
        ("Marigold","Marigold"),
        ("A","A"),
        ("B","B"),
        ("C","C"),
    ]
    section=models.CharField(max_length=64,choices=section_choices)
    subject=models.ManyToManyField(Subject)
    def __str__(self):
        return f"{self.class_name} {self.section}"
class Student(models.Model):
    std_name=models.CharField(max_length=64)
    std_class=models.ForeignKey(Class ,on_delete=models.CASCADE)
    roll_no=models.IntegerField(default=False,null=False,blank=False)
    D_O_B=models.DateField(default=timezone.now)
    admission_date=models.DateField(default=timezone.now)
    parents_name=models.CharField(max_length=64)
    contact=models.CharField(max_length=14)
    def __str__(self):
        return f"{self.std_name}"
    class Meta:
        unique_together=["roll_no","std_class"]