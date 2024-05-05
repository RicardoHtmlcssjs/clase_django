from django.shortcuts import render
# modulo para mostar una respuesta http o algo en pantalla, JsonResponse es un modulo para trabajar con json
from django.http import HttpResponse, JsonResponse
# se estara importando los modelos porject y task para hacer consultas a la base de datos
from .models import Project, Task
# funcion de django permiter obtener un objeto y si no existe mostrar un 404
from django.shortcuts import get_object_or_404
# este seria el archivo principal de la app por que se establece que se va a ejecutar
# Create your views here.
# creacion del hola mundo, se crea una funccion con cual nombre pero recibira un parametro llamado request
def index(request):
    return HttpResponse("<h1>Index page</h1>")

# se resive parametro por get y se estara mostrando en pantalla
def hello(request, username):
    # respuesta http
    return HttpResponse("<h1>Hola %s</h1>" % username)

def project(request):
    # se estara consulta todos los proyectos de la bbdd y se obtiene los valores
    projects = Project.objects.values()
    # se convierte en una lista de python para poder renderizarla
    projects_re = list(projects)
    # JsonResponse() convierte la lista en un json, lleva 2 parametros, 1ro es la lista, 2do safe=False para que sea un objeto serializable
    return JsonResponse(projects_re, safe=False)

# vist que recivira un parametro para asi contultar la task  o tarea en la bbdd
def tasks(request, id):
    # se obtiene por el modelo Task se obtiene por el metodo get el parametro id que sera llamado id
    # si el parametro id no existe mostrar un erro y se caera el servidor
    task_mal = Task.objects.get(id=id)
    # get_object_or_404() este buscara en la bbdd un resultado, lleva 2 parametros: 1ro el modelo a consultar, 2do el parametro a recivir
    task = get_object_or_404(Task, id=id)
    # la vista retorna  task.title es decir el titulo 
    return HttpResponse("<h1>Tasks: %s</h1>" % task.title)