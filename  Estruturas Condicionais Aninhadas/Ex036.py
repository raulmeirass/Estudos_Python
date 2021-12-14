casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int (input('Quanto anos de financiamento? '))
prest = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print (' a prestação será de R${:.2f}'.format(prest)) #end=' ' é para que a frase(a prestação....)vá para cima na mesma linha
sal = (30/100) * salario
if prest > sal :
    print ('Empréstimo NEGADO!')
else:
    print ('Empréstimo pode ser CONCEDIDO')
    
print('    ')
print((prest), (sal))