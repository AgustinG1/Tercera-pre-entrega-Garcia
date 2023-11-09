from django.db import models

# Create your models here.


class Categoria(models.Model):
    CATEGORIAS_CHOICES = (
        ('salada', 'Comida Salada'),
        ('dulce', 'Comida Dulce'),
        ('vegetariana', 'Comida Vegetariana'),
    )

    nombre = models.CharField(
        max_length=100,
        choices=CATEGORIAS_CHOICES,
        default='salada'
    )

    def __str__(self):
        return self.get_nombre_display()

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.receta.titulo}"