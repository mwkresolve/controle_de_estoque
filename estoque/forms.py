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
