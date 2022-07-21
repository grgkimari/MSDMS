from django.shortcuts import render
from django.contrib.auth.forms import  AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        user = form.get_user()
        login(request, user)
        return redirect ('homepage')
    return render(request, 'login.html')

def register_view(request):
    
    return render(request, 'register.html')
