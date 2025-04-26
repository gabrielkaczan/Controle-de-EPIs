from django import forms
from .models import Equipamento, ControleEPI
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = '__all__'

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = '__all__'

class ControleEPIForm(forms.ModelForm):
    class Meta:
        model = ControleEPI
        fields = '__all__'

    def clean_data_prevista_devolucao(self):
        from datetime import date
        data = self.cleaned_data['data_prevista_devolucao']
        if data < date.today():
            raise forms.ValidationError("A data prevista deve ser futura.")
        return data