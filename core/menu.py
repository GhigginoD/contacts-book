from colorama import Fore, Style
from core.banco_de_dados import Bancode
import re


def create_table():
    bd.create_table()


def insert():
    bd.insert_value()


def viewer():
    response = input('''
        1 - Ver todos os dados os dados
        2 - filtrar nome que deseja ver ''')
    if response == '1':
        bd.select_values()
    elif response == '2':
        name = input('Qual nome deseja ver? ')
        bd.select_values_filter(name)
    else:
        print(Fore.RED + 'comando invalido')


def update():
    name = input('Qual o nome do contato a ser alterado?')
    tel = input('Entre com seu novo numero (com DDD) ')
    regex = re.findall('\(?\d{2}\)?\s\d{5}-?\d{4}', tel)
    if regex:
        bd.update_values(name, tel)
    else:
        print(Fore.RED+'Numero invalido')


def apagar():
    response = input(Fore.RED + 'Você está preste a apagar todos, deseja continuar?[s/n]')
    if response == 's':
        bd.drop_table()


bd = Bancode()

while True:
    print(Fore.GREEN + Style.BRIGHT + '''
        0 - Criar novo banco de dados
        1 - Novo contato
        2 - Ver dados
        3 - Atualizar dados
        4 - Apagar dados
        5 - Sair
        ''')

    command = int(input(Fore.BLUE + 'entre com o comando desejado. '))

    if command == 0:
        create_table()
    elif command == 1:
        insert()
    elif command == 2:
        viewer()
    elif command == 3:
        update()
    elif command == 4:
        apagar()
    elif command == 5:
        print(Fore.GREEN + 'Saindo...')
        break
    else:
        print(Fore.RED + 'comando invalido')
