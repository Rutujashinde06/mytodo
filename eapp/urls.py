from django.urls import path
from eapp import views

urlpatterns = [
    # path('',views.home),
   # path('','index',views.index),
    path('',views.index),
    path('registration',views.registration),
    path('login',views.login),
    path('addtask',views.addtask),
    path('edittask/<rid>',views.edittask),
    path('deltask/<rid>',views.deltask),
    path('catfilter/<sid>',views.catfilter),
    path('sort/<sv>',views.sort),
    
]


      
