sal = float(input('Qual o salário do funcionário? R$'))
if sal <= 1250.00:
    aum = (sal * 15/100) + sal
else:
    aum = (sal * 10 / 100) + sal
print ('Quem ganhava R${:.2f} passa a ganhar R$ {:.2f}'.format(sal, aum))
