from django.shortcuts import redirect, render
from driver.models import Driver
from reservation.models import Reservation
from reservation.forms import ReservationForm
from datetime import datetime

# Create your views here.
def reservations(request):
    user = request.user
    reservations = Reservation.objects.filter(kullanici = user)
    context = {
        "user":user,
        "reservations":reservations
    }
    return render(request,'reservation/reservations.html',context)  
def createRez(request):
    if request.method == 'POST':
        # Form verilerini al
        form = ReservationForm(request)
        sehir = request.POST.get('sehir')
        baslangic_tarihi = request.POST.get('baslangic_tarihi')
        bitis_tarihi = request.POST.get('bitis_tarihi')
        kisi_sayisi = request.POST.get('kisi_sayisi')

        # Müsait sürücüleri filtrele
        available_drivers = Driver.objects.filter(availability_start__lte=baslangic_tarihi,
                                                availability_end__gte=bitis_tarihi,
                                                calistigi_sehirler=sehir)
        # gunSayisi = (date_n(bitis_tarihi)-date_n(baslangic_tarihi)).days
        tarih1 = datetime.strptime(bitis_tarihi, "%Y-%m-%d")
        tarih2 = datetime.strptime(baslangic_tarihi, "%Y-%m-%d")
        gun_farki = (tarih1 - tarih2).days
        
        #rezervasyonu kaydedelim
        reservation = Reservation(
            sehir = sehir,
            baslangic_tarihi = baslangic_tarihi,
            bitis_tarihi = bitis_tarihi,
            kisi_sayisi = kisi_sayisi,
            kullanici = request.user,
        )
        reservation.save()
        
        #kullancının rezervasyonunu kaydedelim
        user = request.user
        user.reservation = reservation
        user.save()
        
        
        # Sonuçları şablona aktar
        context = {
            'reservation':reservation,
            'available_drivers': available_drivers,
            'driver_count': range(len(available_drivers)),
            'sehir': sehir,
            'baslangic_tarihi': baslangic_tarihi,
            'bitis_tarihi': bitis_tarihi,
            'kisi_sayisi': kisi_sayisi,
            'gunSayisi':gun_farki,
        }
        return render(request, 'reservation/driverList.html', context)
    else:
        form = ReservationForm()

    return render(request,'reservation/createRez.html',{"form":form})
    
def chooseDriver(request,driverusername,rezID):
    driver = Driver.objects.filter(username = driverusername).first()
    user = request.user
    currentRez = Reservation.objects.filter(id = rezID).first()
    baslangic_tarihi = currentRez.baslangic_tarihi
    bitis_tarihi = currentRez.bitis_tarihi
    tarih1 = bitis_tarihi
    tarih2 = baslangic_tarihi
    gun_farki = (tarih1 - tarih2).days
    
    if(currentRez.kullanici == user):
        print("rez")
        currentRez.fiyat = gun_farki * driver.gunluk_tur_fiyati
        currentRez.surucu = driver
        currentRez.save()
        driver.reservation = currentRez
        driver.save()
    return redirect('index')

def deleteRez(request,rezID):
    cRez = Reservation.objects.filter(id=rezID)
    cRez.delete()
    if Driver.objects.filter(username = request.user.username):
        return redirect("driverDash")
    return redirect("reservations")

def onayRez(request,rezID):
    cRez = Reservation.objects.filter(id=rezID).first()
    cRez.onay_durum = True
    cRez.save()
    return redirect("driverDash")
def tamamRez(request,rezID):
    cRez = Reservation.objects.filter(id=rezID).first()
    cRez.onay_durum = False
    cRez.tamam_durum = True
    cRez.save()
    return redirect("driverDash")