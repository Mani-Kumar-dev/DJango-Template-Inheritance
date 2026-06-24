from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo1(request):
    return render(request,"base.html")

def home(request):
    return render(request,"index.html")