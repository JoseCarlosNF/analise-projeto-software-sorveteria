from dataclasses import dataclass

# -------- Aplicação do padrão DECORATORS. Uma das categorias do GoF. ----------

# Utilização do decorator `dataclass` para criar uma classe especial, algo como
# uma struct das linguagens de programação mais clássicas. Com ela nos podemos
# definir como será a estrutura de um pedido, e quais serão os atribuitos
# necessários para formar o padrão.


@dataclass
class Product:
    name: str
    price: float


class IceCream(Product):
    pass


class Additional(Product):
    pass
