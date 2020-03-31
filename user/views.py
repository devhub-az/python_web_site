from django.shortcuts import render,HttpResponse
from .forms import RegisterForm,LoginForm,UserProfileUpdateForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages

def user_register(request):
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

def user_login(request):
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

def user_settings(request):
    about = request.user.userprofile.about
    avatar = request.user.userprofile.avatar
    initial = {'about':about,'avatar':avatar}
    form = UserProfileUpdateForm(initial= initial,instance=request.user ,data=request.POST or None,files=request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=True)
            about = form.cleaned_data.get('about',None)
            avatar = form.changed_data.get('avatar',None)
            user.userprofile.about = about
            user.userprofile.avatar = avatar
            user.userprofile.save()
            print('Burada  mesaj gonderilecek')
            return HttpResponse('Burada yonlendirilecek link bilinecek')
        else:
            print('Melumatlarin dogru olduguna emin olun')
    return render(request,'settings.html',{'form':form})

def password_change(request):
    pass


