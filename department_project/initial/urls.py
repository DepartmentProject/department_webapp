"""department_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = "Index"),
    path('index',views.index, name = "index"),
    path('cse_home', views.cse_home, name = "cse_home"),
    path('cse_syllabus', views.cse_syllabus, name = "cse_syllabus"),
    path('notes', views.notes, name = "notes"),
    path('packages', views.packages, name = "packages"),
    path('cse_home', views.cse_home, name = "cse_home"),
    path('achievements', views.achievements, name = "achievements"),
    path('cse_cgpa', views.cse_cgpa, name = "cse_cgpa"),
    path('contact', views.contact, name = "contact"),
    path('ece_home', views.ece_home, name = "ece_home"),
    path('ece_syllabus', views.ece_syllabus, name = "ece_syllabus"),
    path('ece_cgpa', views.ece_cgpa, name = "ece_cgpa"),
    path('ece_notes', views.ece_notes, name = "ece_notes")
]
