from django.urls import path
from tnp import views
##from tnp.views import uzername

urlpattern = [
    path('',views.index),
    path('',views.func1),
    path('',views.func2),
]