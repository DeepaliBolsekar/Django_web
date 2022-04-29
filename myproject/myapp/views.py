from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context= {
        "variable":"variable_name"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is home page")

