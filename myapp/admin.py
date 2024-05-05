from django.contrib import admin
# se importa los modelos de myapp
from .models import Project, Task
# aqui se agregara el modelo a el panel de administrador
# Register your models here.

# se esta agregando el model al proyecto 
admin.site.register(Project)
admin.site.register(Task)