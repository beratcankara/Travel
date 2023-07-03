from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import nUserLoginForm, DriverLoginForm
from driver.models import Driver
# Create your views here.
def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            print("Driver user bulunamadı.")
            error_message = 'Geçersiz kullanıcı adı veya parola'
            return render(request, 'login/login.html', {'error_message': error_message})
    else:
        return render(request, 'login/login.html')