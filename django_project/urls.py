"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tnp import views
from app1 import views1
from app2 import views2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('func1/', views.func1),
    path('func2/', views.func2),
    # path('',include('tnp.urls')),

    path('func3/', views1.func3),
    path('func4/', views1.func4),
    path('func5/', views1.func5),

    path('func6/', views2.func6),
    path('func7/', views2.func7),
    path('func8/', views2.func8),
]
