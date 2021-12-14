prod = float (input('Qual o preço do produto? R$'))
desc = (prod/100) * 5
custo = prod - desc
print ('O produto que custava {}R$, agora com o desconto de 5% custará {}R$'.format(prod,custo))
print ('O desconto foi de {}R$'.format(desc))


