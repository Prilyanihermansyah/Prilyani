from django import views
from django.contrib import admin
from django.urls import path
from Feb.views import feb
from Fh.views import fh
from Fisip.views import fisip 
from Fk.views import fk
from Fkip.views import fkip
from Fp.views import fp
from Ft.views import ft
from pascasarjana.views import pascasarjana
from Profil.views import profil
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feb/', feb), 
    path('fh/', fh),
    path('fisip/', fisip),
    path('fk/', fk),
    path('fkip/', fkip),
    path('fp/', fp),
    path('ft/', ft),
    path('pascasarjana/', pascasarjana),
    path('profil/', profil),
    path('', views.index),
]