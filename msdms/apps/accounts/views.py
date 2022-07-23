from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate,login,logout

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email = form.cleaned_data.get('email'), password = form.cleaned_data.get('password'))
            if user:
                login(request, user)
                return redirect('homepage')
            else:
                msg = "Invalid credentials"
        else:
            msg = "Form is not valid."


        context = {
            'msg' : msg
        }
        
    else:
        return render(request, 'accounts/login.html')
    

def register_view(request):
    msg = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            msg = "Incorrect login details"
            context = {
                'msg' : msg
            }
            return render(request,'register.html', context)
    else:
        return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return redirect('homepage')
