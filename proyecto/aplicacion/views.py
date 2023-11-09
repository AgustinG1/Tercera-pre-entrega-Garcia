from django.shortcuts import render, redirect
from .models import Categoria, Receta
from .forms import RecetaForm, ComentarioForm
# Create your views here.

def pagina_inicio(request):
    return render(request, 'inicio.html')




def agregar_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            nueva_receta = form.save()
            return redirect('detalle_receta', receta_id=nueva_receta.id)
    else:
        form = RecetaForm()
    
    return render(request, 'agregar_receta.html', {'form': form})





def detalle_receta(request, receta_id):
    receta = Receta.objects.get(pk=receta_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.receta = receta
            nuevo_comentario.save()
            return redirect('detalle_receta', receta_id=receta.id)

    else:
        form = ComentarioForm()

    comentarios = receta.comentario_set.all()
    
    return render(request, 'detalle_receta.html', {'receta': receta, 'comentarios': comentarios, 'form': form})

def ver_recetas(request):
    query = request.GET.get('q', '')  
    recetas = Receta.objects.filter(titulo__icontains=query) if query else Receta.objects.all()
    return render(request, 'recetas.html', {'recetas': recetas, 'query': query})
