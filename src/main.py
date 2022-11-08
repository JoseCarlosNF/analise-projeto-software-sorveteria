from dataclasses import dataclass

# -------- Aplicação do padrão DECORATORS. Uma das categorias do GoF. ----------

# Utilização do decorator `dataclass` para criar uma classe especial, algo como
# uma struct das linguagens de programação mais clássicas. Com ela nos podemos
# definir como será a estrutura de um pedido, e quais serão os atribuitos
# necessários para formar o padrão.


@dataclass
class Product:
    price: str
    category: str


@dataclass
class ItemOrder:
    item: Product
    flavor: str
    aditional: bool
    aditionais: list


# A seguir, temos a classe `Order`, que manipula os items de um pedido.
class Order:
    def __init__(self, costumer: str, items: list[Product]):
        self.costumer = costumer
        self.items = items

    def add_item(self):
        pass

    def remove_item(self):
        pass

    def finalize(self):
        pass


if __name__ == '__main__':
    pass
