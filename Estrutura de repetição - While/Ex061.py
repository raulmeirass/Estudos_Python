print('GERAÇÃO DE UMA PA')
print('-=' * 15)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('progressão finalizada com {} termos'.format(total))
