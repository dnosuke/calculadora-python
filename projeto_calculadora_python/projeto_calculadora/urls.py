from django.contrib import admin
from django.urls import path
from app_calculadora import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #rota, view,  responsavel, nome de referencia
    path('calculadora/', views.calcular_soma, name='calculadora'),
]
