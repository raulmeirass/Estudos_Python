cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
       'oito', 'nove', 'dez,' 'onze', 'doze', 'treze', 'catorze', 'quinze',
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = ''
while resp != 'N':
    num = int(input('Digite um número: '))
    if 0 <= num <= 20:
        print(f'Voce digitou o número {cont[num]}')
        resp = str(input('Voce quer de novo? [S/N] ')).strip().upper()[0]
    else:
        print('Tente novamente. ', end='')
