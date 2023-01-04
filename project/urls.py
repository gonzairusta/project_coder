"""""project URL Configuration
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (index, saludar_a, sumar, 
                            buscar, monstrar_familiares,
                            BuscarFamiliar, AltaFamiliar,
                            ActualizarFamiliar, BorrarFamiliar,
                            FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar, FamiliarDetalle)
from mundial.views import (index, PostDetalle, PostListar, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout, 
                               AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle )
from django.contrib.admin.views.decorators import staff_member_required
from mundial.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar-a/<nombre>/', saludar_a),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('buscar/',buscar),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('success_updated_message/',TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
    path('mundial/', index, name="mundial-index"),
    path('mundial/<int:pk>/detalle/', PostDetalle.as_view(), name="mundial-detalle"),
    path('mundial/listar/', PostListar.as_view(), name="mundial-listar"),
    path('mundial/crear/', staff_member_required(PostCrear.as_view()), name="mundial-crear"),
    path('mundial/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="mundial-borrar"),
    path('mundial/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="mundial-actualizar"),
    path('mundial/signup/', UserSignUp.as_view(), name ="mundial-signup"),
    path('mundial/login/', UserLogin.as_view(), name= "mundial-login"),
    path('mundial/logout/', UserLogout.as_view(), name="mundial-logout"),
    path('mundial/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="mundial-avatars-actualizar"),
    path('mundial/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="mundial-users-actualizar"),
    path('mundial/mensajes/crear/', MensajeCrear.as_view(), name="mundial-mensajes-crear"),
    path('mundial/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="mundial-mensajes-detalle"),
    path('mundial/mensajes/listar/', MensajeListar.as_view(), name="mundial-mensajes-listar"),
    path('mundial/about', about, name="mundial-acerca-de"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
