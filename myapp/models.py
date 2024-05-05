from django.db import models

# aqui se crean las clases de aplicacion
# Create your models here.
# esto creara una tabla llamada myapp-project y con los campos que espesifique la clase. creara un archivo dentro de la carpeta de migrations donde se espesificaran las caracteristicas de la base de datos
class Project(models.Model):
    # este sera un texto o varchar
    name = models.CharField(max_length=200)
    # creacion de metodo para mostrar en la vista en el panel de administrador, esta mostrar el nombre de los proyectos
    def __str__(self):
        return self.name
# clase que creara una tabla llamada task 'tareas' esta tendra 4 columnas: id, title, despription y project que sera una llave foranea
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # relacionando columnas chaci es automatico lo relaciona con el id, ForeignKey()tendra 2 parametros: 1ro con que se va a relacionar, 2do es opcional orita tendra eliminacion en cascada
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    # metodo para mostrar las Task por el title
    done = models.BooleanField(default=False)
    def __str__(self):
        # se mostrar el titulo de de la Task y concadenato a que nombre de proyecto pertenece
        return self.title + " - " + self.project.name