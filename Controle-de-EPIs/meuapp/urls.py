from django.contrib import admin
from django.urls import path, include
from meuapp import views  # importa a view index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # <-- aqui mapeia a raiz
    path('colaboradores/cadastrar/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('colaboradores/editar/<int:id>/', views.editar_colaborador, name='editar_colaborador'),
    path('colaboradores/excluir/<int:id>/', views.excluir_colaborador, name='excluir_colaborador'),
    path('colaboradores/relatorio/', views.relatorio_colaborador, name='relatorio_colaborador'),
    path('equipamentos/cadastrar/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
    path('controle_epi/', views.controle_epi, name='controle_epi'),
    path('colaboradores/', views.listar_colaboradores, name='listar_colaboradores'),
    path('equipamentos/', views.listar_equipamentos, name='listar_equipamentos'),
]