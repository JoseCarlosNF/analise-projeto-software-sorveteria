from dataclasses import dataclass

# -------- Aplicação do padrão DECORATORS. Uma das categorias do GoF. ----------

# Utilização do decorator `dataclass` para criar uma classe especial, algo como
# uma struct das linguagens de programação mais clássicas. Com ela nos podemos
# definir como será a estrutura de um pedido, e quais serão os atribuitos
# necessários para formar o padrão.

@dataclass
class Produto:
    nome: str
    preco: float
    categoria: str

# A seguir, temos a construção da principal classe 
class Pedido:
    def __init__(self, nome_cliente: str, lista_produto: list):
        self.nome_cliente = nome_cliente
        self.lista_produto = lista_produto

