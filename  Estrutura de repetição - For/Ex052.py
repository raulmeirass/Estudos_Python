num = int(input('Digite um número: '))
div = 0
for c in range (1, num+1):
    if num % c != 0:
        print('{}{}{}'.format('\033[36m', c, '\033[m'), end=' ')
    if num % c == 0:
        print('{}{}{}'.format('\033[31m', c, '\033[m'), end=' ')
        div = div + 1
print('\nO {} foi divisivel {} vezes.'.format(num, div))
if div == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')