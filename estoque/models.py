from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    barcode = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.PositiveIntegerField(default=0)
    data_fabricacao = models.DateField()
    data_validade = models.DateField()

    def __str__(self):
        return f"Produto: {self.nome} - Descrição: {self.descricao} - Barcode: {self.barcode} - Quantidade: {self.quantidade} - Data de Fabricação: {self.data_fabricacao} - Data de Validade: {self.data_validade}"

class EnderecoEstoque(models.Model):
    RUA_CHOICES = [(str(i), str(i)) for i in range(1, 11)]
    ANDAR_CHOICES = [(chr(i), chr(i)) for i in range(ord('A'), ord('Z')+1)]
    PRATELEIRA_CHOICES = [(str(i), str(i)) for i in range(1, 51)]

    rua = models.CharField(max_length=2, choices=RUA_CHOICES)
    andar = models.CharField(max_length=1, choices=ANDAR_CHOICES)
    prateleira = models.CharField(max_length=2, choices=PRATELEIRA_CHOICES)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)

    def __str__(self):
        return f"Rua {self.rua}, Andar {self.andar}, Prateleira {self.prateleira}"
