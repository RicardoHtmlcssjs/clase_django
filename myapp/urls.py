# aqui se espesificara larutas de esta aplicacion para ponerlas todas en el urls.py  del proyecto
# importacion de paquete para establecer rutas
from django.urls import path
from . import views
# arreglo que tendra las rutas de esta aplicacion
urlpatterns = [
    path('', views.index),
    # param aqui se permitira recivir parametros por get, <>  es para recivir parametros pero tiene que, espesificarse que tipo de dato es y  luego se le pone nombre d euna variable dentro que podra ser cualquiera, se le debe asigna a la vita como un 2do parametro el nombre de la variable
    path('hello/<str:username>', views.hello),

    path('tasks/<int:id>', views.tasks),
    path('project', views.project),
]