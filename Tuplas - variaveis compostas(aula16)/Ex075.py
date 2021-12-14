num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Voce digitou os valores {num}')
print(f'o valor 9 aparece {num.count(9)} vezes') #count para contar qnts vezes aparece tal coisa
if 3 in num:
    print(f'O valor 3 apareceu na posição {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram ', end = '')
for n in num:
    if n % 2 == 0:
        print(n, end='')


