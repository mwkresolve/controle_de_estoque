from django import forms
from .models import Produto
class DateInput(forms.DateInput):
    input_type = 'date'

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'data_fabricacao': DateInput(),
            'data_validade': DateInput(),
        }


class EditarProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'data_fabricacao': forms.DateInput(attrs={'type': 'date'}, format='%d/%m/%Y'),
            'data_validade': forms.DateInput(attrs={'type': 'date'}, format='%d/%m/%Y'),
        }
