from django import forms
from .models import Receta, Comentario
from ckeditor.widgets import CKEditorWidget

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'subtitulo', 'categoria', 'ingredientes', 'instrucciones', 'imagen']
        widgets = {
            'ingredientes': CKEditorWidget(),  
            'instrucciones': CKEditorWidget(),  
        }



class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': CKEditorWidget(),
        }