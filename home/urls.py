
from django.urls import path, include
from . import views

urlpatterns = [
   
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),  # we can add / - not necessory 
    path('contact',views.contact,name='contact'),
    path('doctors',views.doctors,name='doctors'),
    path('departments',views.departments,name='departments')

]
