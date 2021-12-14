pesos = []
for pessoas in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoas)))
    pesos.append(peso)
print('O maior peso é {}Kg'.format(max(pesos)))
print('O menor peso é {}Kg'.format(min(pesos)))
