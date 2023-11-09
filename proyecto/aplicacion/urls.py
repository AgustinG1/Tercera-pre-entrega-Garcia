from django.urls import path
from . import views
from .views import agregar_receta, detalle_receta


urlpatterns = [
    path('', views.pagina_inicio, name='inicio'),
    path('agregar_receta/', agregar_receta, name='agregar_receta'),
    path('detalle_receta/<int:receta_id>/', detalle_receta, name='detalle_receta'),
    path('recetas/', views.ver_recetas, name='ver_recetas'),
    
]