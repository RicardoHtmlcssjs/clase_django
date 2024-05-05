# se estara utilizando el paquete form para crear u validar formularios con python
from django import forms

# clase que creara el formulario, tiene que recivir este parametro para poder mostrar el formulario de pantalla
class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de la tarea", max_length=200)
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea)
