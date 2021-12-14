sal = float (input('Qual o salário do funcionário? R$'))
aumento = (sal * 15)/100
novo = sal + aumento
print ('Um funcionário que ganhava {}R$, com o aumento de 15%, passa a ganhar {:.2f}R$'.format (sal, novo))
print ('O aumento foi de {:.2f}R$'.format(aumento))
