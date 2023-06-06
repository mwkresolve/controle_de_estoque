from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm
from .models import Produto
from django.contrib import messages
from django.core.paginator import Paginator

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
def produtos_cadastrados(request):
    sort = request.GET.get('sort', 'nome')  # Obtém o parâmetro de ordenação da query string, padrão é "nome"
    produtos = Produto.objects.order_by(sort)  # Ordena os produtos de acordo com o campo selecionado
    # Configuração da paginação
    paginator = Paginator(produtos, 20)  # Exibe 20 produtos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'produtos':produtos}
    return render(request, 'produtos_cadastrados.html', context)
def produto_delete(request, pk):
    produto = Produto.objects.get(pk=pk)
    produto.delete()
    messages.success(request, 'Produto deletado com sucesso.')
    return redirect('produtos_cadastrados')

