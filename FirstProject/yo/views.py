from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello I am sakib")

def about(request):
    return HttpResponse("No much o know about me")

def contact(request):
    return HttpResponse("01521766283")
