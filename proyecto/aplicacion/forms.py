from django import forms
from .models import Receta, Comentario

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'categoria', 'ingredientes', 'instrucciones']
        

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']
    
    widgets = {
        'autor': forms.TextInput(attrs={'class': 'form-control'}),
        'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
    }