import sqlite3 as sql
from contextlib import closing
import rstr
from colorama import Fore


class Bancode:

    def __init__(self):
        self.contates = []

    @staticmethod
    def create_table():
        with sql.connect('agenda.bd') as connection:
            with closing(connection.cursor()) as cursor:
                try:
                    cursor.execute('create table agenda(name,tel)')
                    connection.commit()
                    print(Fore.YELLOW + 'Banco de Dados criado')
                except:
                    print(Fore.RED + 'Erro ao criar tabela')

    def insert_value(self):
        self.set_contates()
        with sql.connect('agenda.bd') as connection:
            with closing(connection.cursor()) as cursor:
                for contate in self.contates:
                    cursor.execute('insert into agenda(name,tel) values(?,?)', contate)
                connection.commit()
        print(Fore.YELLOW + 'Dados inseridos')

    @staticmethod
    def select_values():
        with sql.connect('agenda.bd') as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('select * from agenda')
                results = cursor.fetchall()
                if not results:
                    print(Fore.RED + 'Banco de Dados Vazio')
                for result in results:
                    print(Fore.YELLOW + 'Nome: %s\nTel: %s\n' % result)

    @staticmethod
    def get_random_tel():

        return ('({0}) {1}-{2}'.format(
            rstr.rstr('1234567890', 2),
            rstr.rstr('1234567890', 5),
            rstr.rstr('1234567890', 4)))

    def set_contates(self):
        name = str(input('Entre com o nome:')).strip()
        number_tel = self.get_random_tel()
        self.contates = [(name, number_tel)]

    @staticmethod
    def select_values_filter(name):
        with sql.connect('agenda.bd') as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('select * from agenda where name = ?', (name,))
                results = cursor.fetchall()
                if not results:
                    print(Fore.RED + 'Nome não encontrado')
                    return 0

                for result in results:
                    print(Fore.YELLOW + 'Nome: %s\nTel: %s' % result)
                    return 1

    def update_values(self, name, tel):
        with sql.connect('agenda.bd') as connection:
            with closing(connection.cursor()) as cursor:
                verify = self.select_values_filter(name)
                if verify == 1:
                    cursor.execute('update agenda set tel = ? where name = ?', (tel, name,))
                    connection.commit()
                    print(Fore.YELLOW + '\nDados alterados para \nNome: {}\nTel: {}'.format(name, tel))

    @staticmethod
    def drop_table():
        with sql.connect('agenda.bd') as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('delete from agenda')
                connection.commit()
                print(Fore.RED + 'Dados Apagados')
