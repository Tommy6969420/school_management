from django.urls import path
from. import views
urlpatterns = [
    path('std_search/',views.get_student_info,name="std_search"),
    path("search_filter",views.search_filter,name="search_filter"),
    path("",views.billing,name="billing")

    
]
