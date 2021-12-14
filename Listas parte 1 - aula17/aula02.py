'''num = [1, 5, 10]
for n in num:         #pra cada elemento da lista
    print(f'{n}...')

num = [5, 10, 20]
for c, n in enumerate (num):  #enumerate pega as duas variaveis (c e n)
                                #c é a
    print(f'Na posição {c} temos o valor {n}')'''

num = list()
for cont in range (1, 4):
    num.append(int(input('Digite um número: ')))
for c, n in enumerate(num):
    print(f'Na posição {c} temos o valor {n}')
print('FIM!')
