from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def cse_home(request):
    return render(request, "index2.html")