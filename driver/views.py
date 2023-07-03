from django.shortcuts import get_object_or_404, redirect, render
from .models import Driver, Image
from .forms import DriverUpdateForm
from reservation.models import Reservation
# Create your views here.
def getOnaysiz(request):
    driver = Driver.objects.filter(username= request.user.username).first()
    reservations = Reservation.objects.filter(surucu = driver,onay_durum = False,tamam_durum = False)
    return reservations
def getOnayli(request):
    driver = Driver.objects.filter(username= request.user.username).first()
    reservations = Reservation.objects.filter(surucu = driver,onay_durum = True,tamam_durum = False)
    return reservations
def getArsiv(request):
    driver = Driver.objects.filter(username= request.user.username).first()
    reservations = Reservation.objects.filter(surucu = driver,onay_durum = False,tamam_durum = True)
    return reservations
    
def getRezID(request):
    driver = Driver.objects.filter(username= request.user.username).first()
    reservations = Reservation.objects.filter(surucu = driver)
    return reservations
    
def driverProfile(request,username):
    driver = Driver.objects.filter(username = username).first()
    getdriverImages = Image.objects.filter(driver=driver)
    driverImages = []
    for image in getdriverImages:
        driverImages.append(image.images)
    context = {
        "driver" : driver,
        "driverImages":driverImages,
        "username":username,
    }
    return render(request,'driver/driverProfile.html',context)
def driverDash(request):
    driver = Driver.objects.filter(username = request.user.username).first()
    reservations = getRezID(request)
    context = {
        "driver":driver,
        "reservations":reservations,
        "onaysizCount":getOnaysiz(request).count(),
        "onayliCount":getOnayli(request).count(),
        "arsivCount":getArsiv(request).count(),
    }
    return render(request,"driver/driverDash.html",context)
def onaysizRez(request):
    driver = Driver.objects.filter(username = request.user.username).first()
    reservations = getRezID(request)
    context = {
        "driver":driver,
        "reservations":reservations,
    }
    return render(request,"reservation/dash/onaysizRez.html",context)
def onayliRez(request):
    driver = Driver.objects.filter(username = request.user.username).first()
    reservations = getRezID(request)
    context = {
        "driver":driver,
        "reservations":reservations,
    }
    return render(request,"reservation/dash/onayliRez.html",context)
def rezArsiv(request):
    driver = Driver.objects.filter(username = request.user.username).first()
    reservations = getRezID(request)
    context = {
        "driver":driver,
        "reservations":reservations,
    }
    return render(request,"reservation/dash/rezArsiv.html",context)

def driverPManage(request):
    driver = get_object_or_404(Driver, username = request.user.username)
    if request.method == "POST":
        form = DriverUpdateForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect("driverDash")
        return redirect("index")
    else:
        form = DriverUpdateForm(instance=driver)
        return render(request,"driver/driverPManage.html",{"driver":driver,"form":form})