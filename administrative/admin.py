from django.contrib import admin
from .models import Class, Student, Subject
# Register your models here.
# admin.site.register(Class)

admin.site.register(Subject)
class ClassAdmin(admin.ModelAdmin):
    list_display=["class_name","section"]
    list_filter=[
        "class_name",
        "section"
    ]
    fields=[("class_name","section"),"subject"]
class StudentAdmin(admin.ModelAdmin):
    list_display=["std_name","std_class","roll_no"]
    list_filter=[
        "std_name","std_class",
    ]
    ordering=("roll_no",)
    search_fields = ['std_name','std_class', ]
    fields=[("std_name","std_class"),"roll_no",("D_O_B","admission_date"),("parents_name","contact")]
admin.site.register(Class,ClassAdmin)
admin.site.register(Student,StudentAdmin)