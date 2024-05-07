# aqui se espesificara larutas de esta aplicacion para ponerlas todas en el urls.py  del proyecto
# importacion de paquete para establecer rutas
from django.urls import path
from . import views
# arreglo que tendra las rutas de esta aplicacion
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    # param aqui se permitira recivir parametros por get, <>  es para recivir parametros pero tiene que, espesificarse que tipo de dato es y  luego se le pone nombre d euna variable dentro que podra ser cualquiera, se le debe asigna a la vita como un 2do parametro el nombre de la variable
    path('hello/<str:username>', views.hello),

    path('tasks/<int:id>', views.all_tasks),
    path('all_tasks/', views.all_tasks),
    path('project', views.project),
    path('create_task', views.create_task),
]