from django.forms import ModelForm
from.models import Student,Subject,Class
class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        help_texts={"Help":"All of the fields are required"}
