from django.shortcuts import render
from .models import Seminar
# Create your views here.

def seminar_list(request):
    return render(request,'seminar/seminar_list.html')

def seminar_create(request):
    return render(request,'seminar/seminar_create.html')

def seminar_detail(request,pk):
    return render(request,'seminar/seminar_detail.html')

def seminar_edit(request,pk):
    return render(request,'seminar/seminar_edit.html')


