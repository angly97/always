from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import * 
from main.models import *
from django.contrib import auth


def login_view(request):
    if request.method == "POST":
        id = request.POST["id"]
        pw = request.POST["pw"]
        user = auth.authenticate(request, username=id, password=pw)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'login.html', {'error': '※아이디 혹은 비밀번호가 일치하지 않습니다.'})
        return redirect("home")
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect("home")


def signUp(request):
     if request.method == 'POST':
         if request.POST['password1']== request.POST['password2']:
            user = User.objects.create_user(
                user_name=request.POST['name'],                #실명
                user_nickname=request.POST['nickname'],        #닉네임
                username=request.POST['id'],                   #아이디
                password=request.POST['password1'],            #비밀번호
                user_phone_number=request.POST['phone_number'],   #전화번호
            )
            auth.login(request, user)
            return redirect("home")
            
     else:
         form: UserCreationForm
         return render(request, "signUp.html")

# def idFind(request):
#     return render(request, "idFind.html")    


# def pwFind(request):
#     return render(request, "pwFind.html")   
    
