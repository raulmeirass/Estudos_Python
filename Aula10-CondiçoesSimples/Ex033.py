a = float(input('Primeiro valor: '))
b = float (input('Segundo valor: '))
c = float (input('Terceiro valor: '))
#verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print ('\033[31;47m O menor valor digitado foi: {}\033[m'.format(menor))
print ('  ')
print ('\033[32;47m O maior valor digitado foi: {}\033[m'.format(maior))



