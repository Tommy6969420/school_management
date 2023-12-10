from django.forms import ModelForm
from.models import Student,Subject,Class
class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields="__all__"
       
class SubjectForm(ModelForm):
    class Meta:
        model=Subject
        fields="__all__"
    
class ClassForm(ModelForm):
    class Meta:
        model=Class
        fields="__all__"

          