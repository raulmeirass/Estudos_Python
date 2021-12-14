num = c = total = menor = maior = 0
resp = ' s '
while resp != 'N': #aprendizado concluido.
    num = int(input('Digite um número: '))
    c = c + 1
    total = num + total
    if c == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = total / c
print('Voce digitou {} números e a média entre eles foi {:.2f}'.format(c, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
