print('-' * 40)
print('{:^40}'.format('SUPERMERCADO RAUL'))
print('-' * 40)
total = mais1000 = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont = cont + 1
    total = total + preco
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar [S/N] ')).upper().strip()[0]
    if preco >= 1000:
        mais1000 = mais1000 + 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {mais1000} produtos custando mais que R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

