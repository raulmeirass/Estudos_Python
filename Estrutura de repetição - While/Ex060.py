n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='') #colocar o x se 'c' for maior que 1, s*
    f = f * c                               #senao por o '='
    c = c - 1
print('{}'.format(f))

''' ou
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = facotorial(n)
print('O fatorial de {} é {}'.format(n, f))'''



