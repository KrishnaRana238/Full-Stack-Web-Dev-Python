from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Hello, this is the index page of myapp.")

# Create your views here.
