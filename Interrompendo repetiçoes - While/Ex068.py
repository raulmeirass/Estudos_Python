from random import randint
comput = randint (0,11)
print('-='*15)
print('VAMOS JOGAR PAR OU IMPAR!')
print('-='*15)
total = c = 0
while True:
    num = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar: (P/I) ')).upper().strip()[0]
    if escolha == 'P':
        escolha = 'PAR'
    elif escolha == 'I':
        escolha = 'IMPAR'
    print('-'*30)
    if (num + comput) % 2 == 0:
        total = 'PAR'
    elif (num + comput) %2 == 1:
        total = 'IMPAR'
    print(f'Voce jogou {num} e o computador jogou {comput}. Total de {num + comput} DEU {total}')
    print('-' * 30)
    if total == escolha:
        print('Voce VENCEU!')
        print('Vamos jogar novamente....')
        c = c + 1
    else:
        print('Voce PERDEU!')
        break
    print('-=' * 15)
print(f'GAME OVER! Voce venceu {c} vezes')





