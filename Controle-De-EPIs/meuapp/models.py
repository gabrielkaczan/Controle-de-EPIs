from django.db import models
from django.utils import timezone

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    cargo = models.CharField(max_length=50, default='Operador')

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True, default='TEMP-CODIGO')
    descricao = models.TextField(default='Sem descrição')

    def __str__(self):
        return self.nome

class ControleEPI(models.Model):
    STATUS_CHOICES = [
        ('EMPRESTADO', 'Emprestado'),
        ('EM_USO', 'Em Uso'),
        ('FORNECIDO', 'Fornecido'),
        ('DEVOLVIDO', 'Devolvido'),
        ('DANIFICADO', 'Danificado'),
        ('PERDIDO', 'Perdido'),
    ]

    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data_entrega = models.DateTimeField(default=timezone.now)
    data_prevista_devolucao = models.DateField(default=timezone.now)
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='EMPRESTADO')
    observacao_devolucao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.colaborador.nome} - {self.equipamento.nome}"



from django.utils import timezone

class RegistroAcoes(models.Model):
    tipo_acao = models.CharField(max_length=50)
    descricao = models.TextField()
    usuario = models.CharField(max_length=100, default='Sistema')
    data_hora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.tipo_acao} - {self.usuario} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"
