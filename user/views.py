from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm,LoginForm,UserProfileUpdateForm,UserPasswordChangeForm
from django.contrib.auth import authenticate, login ,logout,update_session_auth_hash
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
            return redirect('post:main-page')
    return render(request,'user/register.html',{'form':form})

def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username,password= password)
            if user is None:
                print('Username ve ya password yalnisdir')
                return render(request,'user/login.html',{'form':form})
            messages.success(request,'Ugurla daxil oldunuz ')
            return redirect('post:main-page')
    return render(request,'user/login.html',{'form':form})

def user_settings(request):
    about = request.user.userprofile.about
    avatar = request.user.userprofile.avatar
    initial = {'about': about , 'avatar': avatar}
    form = UserProfileUpdateForm(initial= initial,instance=request.user ,data=request.POST or None,files=request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=True)
            about = form.cleaned_data.get('about',None)
            avatar = form.cleaned_data.get('avatar',None)
            user.userprofile.about = about
            user.userprofile.avatar = avatar
            user.userprofile.save()
            print('Burada  mesaj gonderilecek')
            return HttpResponse('Burada yonlendirilecek link bilinecek')
        else:
            print('Melumatlarin dogru olduguna emin olun')
    return render(request,'user/settings.html',{'form':form})

def user_password_change(request):
    form = UserPasswordChangeForm(user= request.user,data= request.POST or None)
    if form.is_valid():
        new_password = form.cleaned_data.get('new_password')
        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request,request.user)
        print('Burada sizin mesajiniz')
        return HttpResponse('burada kecid linki')
    return render(request,'user/password_change.html',{'form':form})

def user_logout(request):
    logout(request)
    print('burada sizin mesajiniz')
    return redirect('post:main-page')

