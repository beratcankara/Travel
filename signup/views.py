from django.shortcuts import render, redirect
from django.urls import reverse
from requests import session
from .forms import RegistrationForm, DriverForm, imageForm
from driver.models import Driver, Image
from django.contrib import messages
from django.contrib.auth import login
from nUser.models import nUser
from django.core.mail import send_mail

def signup(request):
    if request.method == 'POST':
        print("Post edildi.")
        form = request.POST
        request.session['first_name'] = request.POST.get("first_name")
        request.session['last_name'] = request.POST.get("last_name")        
        if 'userSign' in request.POST:
            # Diğer form alanlarındaki değerleri de alabilirsiniz
            return redirect("userSign")
        elif 'driverSign' in request.POST:
            print("driver sign.") 
            return redirect("driverSign")
            
    else:
        form = RegistrationForm()
    return render(request, 'signup/signup.html', {'form': form})


def userSign(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)  # login fonksiyonunu kullanarak giriş yapma işlemi
            messages.success(request, "Başarıyla kayıt olundu.")
            send_mail(
                'Kayıt Olundu',  # E-posta konusu
                'Tebrikler, başarıyla kayıt oldunuz.',  # E-posta içeriği
                'traveldjango@outlook.com',  # Gönderen e-posta adresi
                ['keylogger5534@gmail.com'],  # Alıcı e-posta adresi veya adresleri (bir liste olarak)
                fail_silently=False,  # E-posta gönderimi başarısız olursa hata fırlatılıp fırlatılmayacağı
            )

            return redirect("index")
        else:
            context = {
                "form": form
            }
            return render(request, 'signup/userSign.html', context)
    else:
        form = RegistrationForm()
        first_name = request.session.get("first_name")
        last_name = request.session.get("last_name")
        context = {"first_name": first_name, "last_name": last_name, "form": form}
        return render(request, 'signup/userSign.html', context)
    
def driverSign(request):
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        imageform = imageForm(request.POST, request.FILES)
        files = request.FILES.getlist('images')
        if form.is_valid():
            print("formvalid")
            driver = form.save(commit=False)
            driver.save()
            user = nUser.objects.create_user(username=request.POST["username"],first_name=request.POST["ad"],last_name=request.POST["soyad"],isDriver = True)
            user.set_password(request.POST["password"])
            user.save()
            for image in files:
                Image.objects.create(driver = driver, images=image)
            login(request, user)  # login fonksiyonunu kullanarak giriş yapma işlemi
            messages.success(request, "Başarıyla kayıt olundu.")
            return redirect("index")
        else:
            print("form not valid", form.errors)
            first_name = request.session.get("first_name")
            last_name = request.session.get("last_name")
            context = {
                "first_name": first_name,
                "last_name": last_name,
                "form": form,
                "imagesForm":imageform,
            }
            return render(request, 'signup/driverSign.html', context)
    else:
        form = DriverForm()
        imagesForm = imageForm()
        first_name = request.session.get("first_name")
        last_name = request.session.get("last_name")
        context = {"first_name": first_name, "last_name": last_name, "form": form,"imagesForm":imagesForm}
        return render(request, 'signup/driverSign.html', context)
    
