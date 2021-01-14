import  os

while True:
    nome = input('digite um nome')
    c=0
    while c<5:
        print(nome, 'vc é um programador')
        c+=1
    os.system('clear')