from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def cse_home(request):
    return render(request, "cse.html")

def cse_syllabus(request):
    return render(request, "cse_syllabus.html")