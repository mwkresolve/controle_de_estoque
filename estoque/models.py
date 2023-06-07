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
