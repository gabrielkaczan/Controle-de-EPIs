from django.shortcuts import render, redirect, get_object_or_404
from .models import Colaborador, Equipamento, ControleEPI
from .forms import ColaboradorForm, EquipamentoForm, ControleEPIForm
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# CADASTRAR COLABORADOR
def cadastrar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso!')
            return redirect('cadastrar_colaborador')
        else:
            messages.error(request, 'Erro ao cadastrar colaborador.')
    else:
        form = ColaboradorForm()
    return render(request, 'cadastrar_colaborador.html', {'form': form})

# EDITAR COLABORADOR
def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('cadastrar_colaborador')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'cadastrar_colaborador.html', {'form': form})

# EXCLUIR COLABORADOR
def excluir_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    colaborador.delete()
    messages.success(request, 'Colaborador excluído com sucesso!')
    return redirect('cadastrar_colaborador')

# RELATÓRIO DE EQUIPAMENTOS POR COLABORADOR
def relatorio_colaborador(request):
    nome = request.GET.get('nome')
    emprestimos = ControleEPI.objects.filter(colaborador__nome__icontains=nome) if nome else []
    return render(request, 'relatorio_colaborador.html', {'emprestimos': emprestimos, 'nome': nome})

# CADASTRAR EQUIPAMENTO
def cadastrar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento cadastrado com sucesso!')
            return redirect('cadastrar_equipamento')
        else:
            messages.error(request, 'Erro ao cadastrar equipamento.')
    else:
        form = EquipamentoForm()
    return render(request, 'cadastrar_equipamento.html', {'form': form})

# CONTROLE DE EPI
def controle_epi(request):
    if request.method == 'POST':
        form = ControleEPIForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro de EPI criado com sucesso!')
            return redirect('controle_epi')
        else:
            messages.error(request, 'Erro ao registrar EPI.')
    else:
        form = ControleEPIForm()
    return render(request, 'controle_epi.html', {'form': form})

def listar_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'colaborador.html', {'colaboradores': colaboradores})

def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamento.html', {'equipamentos': equipamentos})