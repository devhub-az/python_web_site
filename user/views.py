from django.shortcuts import render
from .forms import RegisterForm



def register(request):
    form = RegisterForm(request.POST or None)
    return render(request,'register.html',{'form':form})
