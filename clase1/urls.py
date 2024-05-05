"""
URL configuration for clase1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# include es para incluir en este rutas de otro archivo creado
from django.urls import path, include

urlpatterns = [
    # ruta para el panel de administrador
    path('admin/', admin.site.urls),
    # al colocarle el string vacio quiere decir que ante de estas url no va a ir nada, y lo quetenga a le va precidor a la las rutas establecidas en la aplicacion que tiene el include
    path('', include('myapp.urls')),
]
