'''s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print(f'A soma vale {s}') #esse "f" é uma fs tring'''
nome = 'Raul'
idade = 17
print(f'O {nome:^10} tem {idade} anos') #"nome: 10" é para colocar raul em 10 espaços e
                                        #o ^ é para centralizar
                                        #"nome: -^10" seria para colocar o nome em 10 espaços
                                                 #e no meio de  "-"