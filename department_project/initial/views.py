from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def cse(request):
    return render(request, "cse.html")