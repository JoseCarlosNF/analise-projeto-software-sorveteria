# Sorveteria

```
                          Universidade Federal do Pará
                    Instituto de Ciências Exatas e Naturais
                            Faculdade de Computação
                      Bacharelado em Ciência da Computação
                         Análise e Projetos de Software

                   Aluno: Jose C. N. Ferreira - 201804940020

                     Implementação Questão 1 - 2a Avaliação
```

Em resumo temos 3 classes principais:

  - Product
    - Additional
    - IceCream
  - ItemOrder
  - Order

As classes Additional e IceCream são herdeiras de Product.

E a classe Order, agrupa todos os elementos que um pedido pode ter.

E esses elementos, podem conter os adicionais, de maneira que sejam compostos
pela combinação, valor cobrado no recipiente em questão mais o valor dos
adicionais.

## Execução

Ao executar o  `main.py`, teremos a simulação não interativa de um pedido e seus
componentes.

Resultando na saida a seguir:

```
----- Items do pedido -----
[ItemOrder(item=IceCream(name='casquinha', price=1.5),
           flavor='morango',
           additional=[Additional(name='cobertura de chocolate', price=0.5),
                       Additional(name='cobertura de caramelo', price=0.5)]),
 ItemOrder(item=IceCream(name='taca', price=0),
           flavor='cupuaçu',
           additional=[Additional(name='cobertura de morango', price=0.5)]),
 ItemOrder(item=IceCream(name='copo', price=0.2),
           flavor='bacuri',
           additional=[Additional(name='cobertura de caramelo', price=0.5)])]

----- Custo total do pedido -----
'R$ 3.70'
```
