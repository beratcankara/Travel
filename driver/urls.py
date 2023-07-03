from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import views 
from django.conf import settings

urlpatterns = [
    path('driverprofile/<str:username>',views.driverProfile,name='driverProfile'),
    path('driverDash/',views.driverDash,name='driverDash'),
    path('driverDash/onaysızRez/',views.onaysizRez,name='onaysizRez'),
    path('driverDash/onaylıRez/',views.onayliRez,name='onayliRez'),
    path('driverDash/rezArsiv/',views.rezArsiv,name='rezArsiv'),
    path('driverDash/manageProfil/',views.driverPManage,name='manageProfil'),
    
    
]
