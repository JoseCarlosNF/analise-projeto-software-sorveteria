from pprint import pprint

from models.product import Additional, IceCream
from order import ItemOrder, Order

if __name__ == '__main__':
    copo = IceCream('copo', 0.2)
    taca = IceCream('taca', 0)
    casquinha = IceCream('casquinha', 1.5)

    cobertura_chocolate = Additional('cobertura de chocolate', 0.5)
    cobertura_morango = Additional('cobertura de morango', 0.5)
    cobertura_caramelo = Additional('cobertura de caramelo', 0.5)

    order = Order(
        'Joselito',
        [
            ItemOrder(
                casquinha, 'morango', [cobertura_chocolate, cobertura_caramelo]
            ),
            ItemOrder(taca, 'cupuaçu', [cobertura_morango]),
            ItemOrder(copo, 'bacuri', [cobertura_caramelo]),
        ],
    )

    print(f'{5*"-":<5}', 'Items do pedido', f'{5*"-":>5}')
    pprint(order.list)

    print('\n----- Custo total do pedido -----')
    pprint(f'R$ {order.finalize():.2f}')
