from django.contrib import admin
from django.urls import path
from base.views import inicio, contato, reserva

urlpatterns = [
    path('', inicio),
    path('contato/', contato),
    path('reserva/', reserva, name='reserva'),
    path('admin/', admin.site.urls),
]
