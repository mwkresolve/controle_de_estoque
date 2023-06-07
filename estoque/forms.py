from django import forms
from .models import Produto, EnderecoEstoque
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
        error_messages = {
            'barcode': {
                'unique': 'Já existe um produto cadastrado com este código de barras.',
            }}


class EditarProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'data_fabricacao': forms.DateInput(attrs={'type': 'date'}, format='%d/%m/%Y'),
            'data_validade': forms.DateInput(attrs={'type': 'date'}, format='%d/%m/%Y'),
        }




class EnderecarProdutoForm(forms.Form):
    produto = forms.ModelChoiceField(queryset=Produto.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label='Produto',
                                     to_field_name='id',
                                     empty_label=None,
                                     required=True,
                                     help_text='Selecione o produto a ser endereçado')
    rua = forms.IntegerField(min_value=1, max_value=10,
                             widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             label='Rua')
    andar = forms.ChoiceField(choices=[(chr(i), chr(i)) for i in range(ord('A'), ord('Z')+1)],
                              widget=forms.Select(attrs={'class': 'form-control'}),
                              label='Andar')
    prateleira = forms.IntegerField(min_value=1, max_value=50,
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                    label='Prateleira')
    quantidade = forms.IntegerField(min_value=0, max_value=500000000000,
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                    label='Quantidade')
