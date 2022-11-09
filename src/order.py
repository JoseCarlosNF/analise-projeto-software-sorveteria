import logging
from dataclasses import dataclass

from models.product import Additional, IceCream

logging.basicConfig(level=logging.ERROR)


# Nessa classe definimos o comportamento de um item do 'carrinho'. Cada um dos
# items pode ter adicionais, e esses adicionais serão atributos do item em
# questão.
@dataclass
class ItemOrder:
    item: IceCream
    flavor: str
    additional: list[Additional]

    @property
    def cost(self):
        """
        Custo de um item do carrinho.

        Esse custo é a soma de todos os adicionais e o preço do item.
        """
        return sum(item.price for item in self.additional) + self.item.price

    @property
    def has_additional(self):
        """
        Indica se um item do carrinho tem adicionais.
        """
        return True if self.additional else False


# Na classe `Order` os items são agrupados para serem efetivamente vendidos.
class Order:
    def __init__(self, costumer: str = None, items: list[ItemOrder] = None):
        self.costumer = costumer
        self.items = items

    def add_item(self, item: ItemOrder):
        try:
            if self.items:
                self.items.append(item)
                logging.info(f'{item} adicionado ao carrinho')
                return self.items
            else:
                return 'Não há items no carrinho.'
        except Exception as error:
            logging.error(
                f'Não foi possível adicionar um novo item ao carrinho. {error}'
            )

    def remove_item(self, index_item: int):
        try:
            if self.items:
                item = self.items.pop(index_item)
                logging.info(f'{item} removido do carrinho')
                return item
            else:
                return 'Não há items no carrinho.'
        except Exception as error:
            logging.error(
                f'Não foi possível remover o item de index {index_item} do carrinho. {error}'
            )

    def finalize(self):
        logging.info(f'Pedido finalizado. Lista de items {self.items}')
        return self.cost

    @property
    def list(self):
        return self.items

    @property
    def cost(self):
        try:
            if self.items:
                return sum(item.cost for item in self.items)
            else:
                return 'Não há items no carrinho.'
        except Exception as error:
            logging.error(
                f'Não foi possível finalizar o pedido {self}. {error}'
            )
