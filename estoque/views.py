from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm

@login_required
def HomePageView(request):
    return render(request, "home.html")

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_inicial')  # redirecionar para a página inicial após o cadastro do produto
    else:
        form = ProdutoForm()

    return render(request, 'cadastrar_produto.html', {'form': form})