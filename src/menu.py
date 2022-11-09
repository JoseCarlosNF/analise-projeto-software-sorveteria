class Menu:
    def __init__(self, options: dict):
        self.options = options

    def read_option(self):
        while True:
            print('--------------------------')
            print(f"{'N°' : <5}{'Descricao' : >5}", end='\n\n')

            for n, option in self.options.items():
                print(f'{n : <5}{option["title"] : >5}')

            print('--------------------------')

            select_option = int(input('Digite o n° da opção: '))
            if select_option == 0:
                break
            elif select_option in self.options.keys():
                self.options[select_option]['action']()
            else:
                print('Opção ínvalida.')


if __name__ == '__main__':

    add_item_menu = Menu(
        {
            1: {'title': 'Selecionar recipiente'},
            3: {'title': 'Selecionar sabor'},
            2: {'title': 'Selecionar adicional'},
            0: {'title': 'Voltar'},
        }
    )

    remove_item_menu = Menu(
        {
            1: {'title': 'Selecionar item'},
            0: {'title': 'Voltar'},
        }
    )

    edit_item_menu = Menu(
        {
            1: {'title': 'Selecionar recipiente'},
            3: {'title': 'Selecionar sabor'},
            2: {'title': 'Selecionar adicional'},
            0: {'title': 'Voltar'},
        }
    )

    main_menu = Menu(
        {
            1: {
                'title': 'Adicionar item',
                'action': add_item_menu.read_option,
            },
            2: {
                'title': 'Remover item',
                'action': remove_item_menu.read_option,
            },
            3: {'title': 'Editar item', 'action': edit_item_menu.read_option},
            0: {'title': 'Finalizar compra'},
        }
    )

    main_menu.read_option()
