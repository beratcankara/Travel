from django.contrib import admin
from django.urls import include, path
from . import views 
urlpatterns = [
    path('',views.reservations,name='reservations'),
    path('createRez/',views.createRez,name='createRez'),
    path('chooseDriver/<str:driverusername>/<str:rezID>',views.chooseDriver,name='chooseDriver'),
    path('deleteRez/<str:rezID>',views.deleteRez,name='deleteRez'),
    path('onayRez/<str:rezID>',views.onayRez,name='onayRez'),
    path('tamamRez/<str:rezID>',views.tamamRez,name='tamamRez'),
    
    
]