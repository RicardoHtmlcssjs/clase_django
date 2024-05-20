from django.contrib import admin
# se importa los modelos de myapp
from .models import Project, Task
# aqui se agregara el modelo a el panel de administrador
# Register your models here.

# aqui se cambia el titulo del header
admin.site.site_header='Minec1'
# cambio del titulo del sistema
admin.site.index_title='Minec2'
# cambio nombre de titulo en la pestaña
admin.site.site_title='Minec3'

# creacion de clase para aespesificar los campos a mostrar en la tabla y un campo de busqueda. poniendole como atribu to a la clase admin.ModelAdmin para poder hacer loscambios
class TaskAdmin(admin.ModelAdmin):
    # date_hierarchy = 'created'
    # list_display: espesifica los campos a mostrar de bbdd, accepted no esta en bbdd es una columna creada dinamicamente, tiene que tener el mismo nombre que el metodo
    list_display=('id', 'title', 'description', 'done', 'accepted','project')
    # search_fields: campos a buscar
    search_fields=('title', 'description')
    # fields: muestra los campos a editar en el order que se escriban
    fields=('title', 'description', 'done', 'project')
    # 
    ordering=('-title', '-description')
    def accepted(self, obj):
        return "aceptado" if obj.done > 0 else "no aceptado"
    icon_name='gamepad'
# se esta agregando el model al proyecto y se le passacomo 2do parametro la clase a modificar
admin.site.register(Task, TaskAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
    search_fields=('id','name')

admin.site.register(Project, ProjectAdmin)
