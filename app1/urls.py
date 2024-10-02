from django.urls import path
from app1 import views1

urlpattern = [
    path('',views1.func3),
    path('',views1.func4),
    path('',views1.func5),
   ## path('',uzername()),
]