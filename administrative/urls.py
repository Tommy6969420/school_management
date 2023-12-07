from django.urls import path
from. import views
urlpatterns = [
    path("students/",views.studentsinfo,name="admission"),\
    path("classes/",views.classesinfo),
    path("students/<id>",views.studentfilter,)
]