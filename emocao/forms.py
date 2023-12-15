from django.forms import ModelForm
from django import forms

from .models.emocao import Emocao

class EmocaoForm(ModelForm):

    class Meta:
        model = Emocao
        fields = '__all__'
        widgets = {
            'motivo' : forms.TextInput(attrs={'class': 'form-control' }),
            'descricao' : forms.TextInput(attrs={'class': 'form-control' }),
            'tipo_emocao' : forms.Select(attrs={'class': 'form-control' }),
        }
        labels = {
            'motivo': 'Motivo',
            'descricao': 'Descrição',
            'tipo_emocao': 'Tipo de Emoção',
        }
