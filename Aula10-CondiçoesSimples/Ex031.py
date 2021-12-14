dist = float(input('Qual é a distancia da sua viagem?'))
if dist <= 200:
    custo = dist * 0.50
else:
    custo = dist * 0.45
print ('Voce esta prestes a começar uma viagem de {}Km.'.format(dist))
print ('E o preço da sua passagem será de R${:.2f}'.format(custo))

'''preço = dist * 0.50 if dist <= 200 else dist * 0.45''' #if simplificado

