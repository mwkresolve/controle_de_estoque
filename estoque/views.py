from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm, EditarProdutoForm, EnderecarProdutoForm
from .models import Produto, EnderecoEstoque
from django.contrib import messages
from django.core.paginator import Paginator
from django import forms

@login_required
def HomePageView(request):
    return render(request, "home.html")

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso.')
            return redirect('cadastrar_produto')
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form': form})

class EditarProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'data_fabricacao': forms.DateInput(attrs={'disabled': True}),
            'data_validade': forms.DateInput(attrs={'disabled': True}),
        }

def produtos_cadastrados(request):
    sort = request.GET.get('sort', 'nome')  # Obtém o parâmetro de ordenação da query string, padrão é "nome"
    direction = request.GET.get('direction', 'asc')  # Obtém o parâmetro de direção da query string, padrão é "asc"

    # Verifica a direção da ordenação
    if direction == 'desc':
        sort = '-' + sort  # Adiciona o sinal de "-" para ordenação decrescente

    produtos = Produto.objects.order_by(sort)  # Ordena os produtos de acordo com o campo selecionado

    # Inverte a direção para o próximo clique
    next_direction = 'asc' if direction == 'desc' else 'desc'

    # Configuração da paginação
    paginator = Paginator(produtos, 20)  # Exibe 20 produtos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'produtos': produtos,
        'sort': sort,
        'next_direction': next_direction,
    }
    return render(request, 'produtos_cadastrados.html', context)

def produto_delete(request, pk):
    produto = Produto.objects.get(pk=pk)
    produto.delete()
    messages.success(request, 'Produto deletado com sucesso.')
    return redirect('produtos_cadastrados')




def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == 'POST':
        form = EditarProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'O produto foi editado com sucesso!')
            form = EditarProdutoForm(instance=produto)  # Reinicializa o formulário com os dados atualizados

    else:
        form = EditarProdutoForm(instance=produto)

    context = {'form': form}
    return render(request, 'editar_produto.html', context)





def enderecar_produto(request):
    if request.method == 'POST':
        form = EnderecarProdutoForm(request.POST)
        if form.is_valid():
            produto_id = form.cleaned_data['produto'].id
            rua = form.cleaned_data['rua']
            andar = form.cleaned_data['andar']
            prateleira = form.cleaned_data['prateleira']

            produto = get_object_or_404(Produto, pk=produto_id)
            endereco = EnderecoEstoque(produto=produto, rua=rua, andar=andar, prateleira=prateleira)
            endereco.save()

            messages.success(request, 'O produto foi endereçado com sucesso.')
            return redirect('enderecar_produto')
    else:
        form = EnderecarProdutoForm()

    return render(request, 'enderecar_produto.html', {'form': form})
