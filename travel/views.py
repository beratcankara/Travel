import json
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from driver.models import Driver
from nUser.models import nUser

from reservation.models import Reservation

# Create your views here.
def index(request):
    print(request.user)
    if request.user == "AnonymousUser":
        user = request.user
        reservations = Reservation.objects.filter(kullanici=user)
        for reservation in reservations:
            if reservation.surucu == None:
                reservation.delete()
            else:
                pass
    return render(request, 'index/index.html')
def logoutV(request):
    logout(request)
    return redirect('index')
def userProfile(request,username):
    user = nUser.objects.filter(username = username).first()
    userRezCount = Reservation.objects.filter(kullanici = user).count()
    return render(request,"user/userProfile.html",{"user":user,"count":userRezCount})
def cities(request):
    with open('static/json/belediyelerfull.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    return render(request,"index/cities.html",{"data":data})