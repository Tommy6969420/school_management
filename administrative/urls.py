from django.urls import path
from. import views
urlpatterns = [
    path("students/",views.studentsinfo,name="students"),
    path("classes/",views.classesinfo,name="classes"),
    path("students/<id>",views.studentfilter,name="students/<id>"),
    path("admission/",views.admission_form,name="admission_form"),
]