from django.shortcuts import render,HttpResponse
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit = False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            login(request,user)
            messages.success(request,'Ugurla qeydiyyatdan keçdiniz')
            return HttpResponse('salam ala')
    return render(request,'user/register.html',{'form':form})

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username,password= password)
            if user is None:
                
                return render(request,'user/login.html',{'form':form})
            messages.success(request,'Ugurla daxil oldunuz ')
            return HttpResponse(':))))))))))))))))')
    return render(request,'user/login.html',{'form':form})