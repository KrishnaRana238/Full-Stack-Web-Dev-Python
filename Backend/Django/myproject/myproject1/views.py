from django.shortcuts import render

# Create your views here.
def myproject1(request):
    return render(request, 'myproject1/index.html')