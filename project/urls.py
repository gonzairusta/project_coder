"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import index, monstrar_familiares, BuscarFamiliar, AltaFamiliar, mostrar_mascotas, mostrar_automoviles, AltaAutomovil, AltaMascota, BuscarAutomovil, BuscarMascota
from ejemplo.views import FamiliarDetalle, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar
from ejemplo_dos.views import index, PostList, PostCrear

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), 
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()), 
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mascotas/', mostrar_mascotas),
    path('mascotas/buscar', BuscarMascota.as_view()),
    path('mascotas/alta', AltaMascota.as_view()),
    path('automoviles/', mostrar_automoviles),
    path('automoviles/buscar', BuscarAutomovil.as_view()),
    path('automoviles/alta', AltaAutomovil.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()), 
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()), 
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()), 
    path('ejemplo-dos/', index, name="ejemplo-dos-index"),
    path('ejemplo-dos/listar/', PostList.as_view(), name="ejemplo-dos-listar"),
    path('ejemplo-dos/crear/', PostCrear.as_view(), name="ejemplo-dos-crear"),





]
