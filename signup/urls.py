from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static  
urlpatterns = [
    path('', views.signup, name='signup'),
    path('usersign/', views.userSign, name='userSign'),
    path('driversign/', views.driverSign, name='driverSign'),   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
